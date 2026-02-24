import tempfile
import os, re, uuid, shutil,json
from google.genai import types
from fastapi import HTTPException, UploadFile
from google import genai

from config import config


try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

try:
    import PyPDF2
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False

UPLOAD_DIR = tempfile.mkdtemp()

def extract_pdf_text(path: str) -> str:
    """Extract text from PDF using pdfplumber, fallback to PyPDF2."""
    text = ""

    if HAS_PDFPLUMBER:
        try:
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    t = page.extract_text()
                    if t:
                        text += t + "\n"
            if text.strip():
                return clean_text(text)
        except Exception:
            pass

    if HAS_PYPDF2:
        try:
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    t = page.extract_text()
                    if t:
                        text += t + "\n"
        except Exception:
            pass

    return clean_text(text)


def clean_text(text: str) -> str:
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]{2,}', ' ', text)
    text = re.sub(r'Page \d+ of \d+', '', text, flags=re.IGNORECASE)
    return text.strip()


def save_upload(file: UploadFile) -> str:
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(400, detail="Only PDF files are accepted.")
    path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.pdf")
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return path


GEMINI_API_KEY = config.GEMINI_API_KEY
GEMINI_MODEL   = config.GEMINI_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)

def call_gemini(prompt: str) -> dict:
    """
    Call Gemini and parse JSON response.
    Returns parsed dict or error dict.
    """
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=types.Part.from_text(text=prompt),
            config=types.GenerateContentConfig(
                temperature=0.0, # low temperature for strict factual extraction
                top_p=0.95,
                top_k=20,
                response_mime_type="application/json", # Native JSON structured output
            ),
        )
        if not response.text:
            raise ValueError("Model returned no text output")
            
        text = response.text.strip()
        # Even with JSON mode, occasionally there are wrapping artifacts depending on model behavior
        text = re.sub(r'^```(?:json)?\s*', '', text, flags=re.MULTILINE)
        text = re.sub(r'^```\s*', '', text, flags=re.MULTILINE)
        text = text.strip()
        
        return json.loads(text)

    except json.JSONDecodeError as e:
        # Fallback regex extraction if pure JSON load fails
        import traceback
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except Exception:
                pass
        return {"error": f"Could not parse Gemini response: {str(e)}", "raw": text[:500], "trace": traceback.format_exc()}

    except Exception as e:
        import traceback
        return {"error": f"Gemini API error: {str(e)}", "trace": traceback.format_exc()}

