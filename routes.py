import os
from typing import Optional
import uuid

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import HTMLResponse

from dash import DASHBOARD_HTML
from prompts import build_chat_prompt, build_full_analysis_prompt, build_lab_only_prompt, build_risk_only_prompt, build_summary_only_prompt
from utils import GEMINI_API_KEY, GEMINI_MODEL, HAS_PDFPLUMBER, HAS_PYPDF2, call_gemini, extract_pdf_text, save_upload
router = APIRouter()


@router.get("/health")
def health():
    """Check API and Gemini connectivity."""
    return {
        "status":       "healthy",
        "model":        GEMINI_MODEL,
        "pdf_engine":   "pdfplumber" if HAS_PDFPLUMBER else ("PyPDF2" if HAS_PYPDF2 else "none"),
        "api_key_set":  GEMINI_API_KEY != "YOUR_GEMINI_API_KEY_HERE",
    }


@router.post("/report/full-analysis")
async def full_analysis(
    file:            UploadFile   = File(..., description="Patient PDF report"),
    age:             Optional[int]   = Form(None, description="Patient age"),
    gender:          Optional[str]   = Form(None, description="male / female"),
    prev_admissions: Optional[int]   = Form(None, description="Previous admissions count"),
):
    """
    🏥 Full AI analysis — everything in one call.
    Returns: patient summary, lab analysis, risk scores, bed management, doctor advice.
    """
    path = save_upload(file)
    try:
        text = extract_pdf_text(path)
        if not text:
            raise HTTPException(422, "Could not extract text from PDF. Use a text-based PDF.")

        extra  = {"age": age, "gender": gender, "prev_admissions": prev_admissions}
        prompt = build_full_analysis_prompt(text, extra)
        result = call_gemini(prompt)

        return {
            "request_id": str(uuid.uuid4()),
            "filename":   file.filename,
            "status":     "success",
            "analysis":   result,
        }
    finally:
        try: os.remove(path)
        except: pass


@router.post("/report/summary")
async def report_summary(
    file: UploadFile = File(..., description="Patient PDF report"),
):
    """
    📄 Get a clean structured summary of a patient report.
    Returns: patient info, chief complaint, history, diagnosis, treatment, recommendations.
    """
    path = save_upload(file)
    try:
        text = extract_pdf_text(path)
        if not text:
            raise HTTPException(422, "Could not extract text from PDF.")

        result = call_gemini(build_summary_only_prompt(text))
        return {
            "request_id": str(uuid.uuid4()),
            "filename":   file.filename,
            "status":     "success",
            "summary":    result,
        }
    finally:
        try: os.remove(path)
        except: pass


@router.post("/report/lab-analysis")
async def lab_analysis(
    file: UploadFile = File(..., description="Patient PDF with lab results"),
):
    """
    🔬 Detect and classify all lab values from a medical report.
    Returns: findings with 🟢🟡🟠🔴 severity, alerts, overall severity.
    """
    path = save_upload(file)
    try:
        text = extract_pdf_text(path)
        if not text:
            raise HTTPException(422, "Could not extract text from PDF.")

        result = call_gemini(build_lab_only_prompt(text))
        return {
            "request_id":   str(uuid.uuid4()),
            "filename":     file.filename,
            "status":       "success",
            "lab_analysis": result,
        }
    finally:
        try: os.remove(path)
        except: pass


@router.post("/report/risk-score")
async def risk_score(
    file:            UploadFile   = File(...),
    age:             Optional[int]   = Form(None),
    gender:          Optional[str]   = Form(None),
    prev_admissions: Optional[int]   = Form(None),
):
    """
    📊 Predict patient readmission risk, complication risk, and appointment priority.
    Returns: risk percentages, priority level, key risk factors, bed recommendation.
    """
    path = save_upload(file)
    try:
        text = extract_pdf_text(path)
        if not text:
            raise HTTPException(422, "Could not extract text from PDF.")

        extra  = {"age": age, "gender": gender, "prev_admissions": prev_admissions}
        result = call_gemini(build_risk_only_prompt(text, extra))
        return {
            "request_id": str(uuid.uuid4()),
            "filename":   file.filename,
            "status":     "success",
            "risk":       result,
        }
    finally:
        try: os.remove(path)
        except: pass


@router.get("/agent/chat")
def agent_chat(message: str):
    """
    💬 Ask the medical AI any clinical question.
    Example: /agent/chat?message=What does high creatinine indicate?
    """
    result = call_gemini(build_chat_prompt(message))
    return {
        "question": message,
        "response": result,
    }


@router.get("/analytics/doctors")
def doctor_analytics():
    """
    📈 Get AI-generated doctor performance insights.
    """
    prompt = """You are QuickCare AI. Generate realistic doctor performance analytics for a hospital.
Return ONLY valid JSON.

Return:
{
  "insights": [
    "📊 Dr. Sharma handles 34% chronic patients vs avg 25% — consider redistribution",
    "⚠️ Dr. Patel readmission rate 28.3% exceeds 25% target",
    "⭐ Dr. Gupta has excellent satisfaction score: 4.7/5"
  ],
  "doctors": [
    {
      "name": "Dr. Sharma",
      "total_patients": 120,
      "avg_diagnosis_time_min": 22,
      "readmission_rate_percent": 18.5,
      "avg_satisfaction": 4.2,
      "chronic_patient_percent": 34,
      "specialty": "Cardiology"
    }
  ]
}
Include 5 realistic doctors with varied specialties and performance metrics."""

    result = call_gemini(prompt)
    return {"status": "success", "analytics": result}


# ─────────────────────────────────────────────────────────────
# BUILT-IN HTML DASHBOARD (served at /)
# ─────────────────────────────────────────────────────────────


@router.get("/", response_class=HTMLResponse)
def dashboard():
    """Serve the built-in QuickCare AI dashboard."""
    return DASHBOARD_HTML