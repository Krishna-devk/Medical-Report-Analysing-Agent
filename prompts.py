import json
def build_lab_only_prompt(report_text: str) -> str:
    return f"""You are QuickCare AI. Extract ALL lab test results from this medical report.
For each result, classify severity using standard medical reference ranges.
Return ONLY valid JSON, no markdown.

REPORT:
\"\"\"
{report_text[:5000]}
\"\"\"

Return:
{{
  "findings": [
    {{
      "parameter": "string",
      "value": 0.0,
      "unit": "string",
      "normal_range": "string",
      "status": "Normal / Mild / Moderate / Critical",
      "emoji": "🟢 / 🟡 / 🟠 / 🔴",
      "flag": "HIGH / LOW / NORMAL"
    }}
  ],
  "overall_severity": "string",
  "overall_emoji": "string",
  "critical_count": 0,
  "moderate_count": 0,
  "mild_count": 0,
  "normal_count": 0,
  "alerts": [],
  "requires_immediate_attention": false
}}"""


def build_risk_only_prompt(report_text: str, extra: dict) -> str:
    return f"""You are QuickCare AI. Assess patient risk from this medical report.
Return ONLY valid JSON, no markdown.

Extra info: {json.dumps(extra)}

REPORT:
\"\"\"
{report_text[:5000]}
\"\"\"

Return:
{{
  "readmission_risk_percent": 0,
  "complication_risk_percent": 0,
  "overall_risk_level": "Low / Medium / High / Very High",
  "risk_emoji": "🟢 / 🟡 / 🟠 / 🔴",
  "appointment_priority": "NORMAL / MEDIUM / HIGH / URGENT",
  "priority_color": "green / yellow / orange / red",
  "priority_message": "string",
  "key_risk_factors": [],
  "requires_alert": false,
  "bed_management": {{
    "recommended_ward": "string",
    "estimated_stay_days": 0,
    "discharge_note": "string"
  }}
}}"""


def build_chat_prompt(question: str) -> str:
    return f"""You are QuickCare AI, a clinical intelligence assistant for doctors and hospital staff.
Answer the following medical question clearly and concisely.
Return ONLY valid JSON with key "answer".

Question: {question}

Return: {{"answer": "your detailed answer here"}}"""



def build_full_analysis_prompt(report_text: str, patient_extra: dict) -> str:
    extra_info = ""
    if patient_extra.get("age"):
        extra_info += f"\nPatient Age (user provided): {patient_extra['age']}"
    if patient_extra.get("gender"):
        extra_info += f"\nPatient Gender (user provided): {patient_extra['gender']}"
    if patient_extra.get("prev_admissions"):
        extra_info += f"\nPrevious Admissions: {patient_extra['prev_admissions']}"

    return f"""You are QuickCare AI, an expert clinical intelligence system used by hospital doctors.
Analyze the following patient medical report carefully and return a single valid JSON object.
Do NOT include any explanation, markdown formatting, or text outside the JSON.

{extra_info}

PATIENT MEDICAL REPORT:
\"\"\"
{report_text[:5000]}
\"\"\"

Return this EXACT JSON structure. Fill every field based on the report content.
If information is not present, use sensible defaults (null for numbers, "Not mentioned" for strings).

{{
  "patient_info": {{
    "name": "Patient full name or Unknown",
    "age": null,
    "gender": "Male / Female / Unknown",
    "patient_id": "ID if present or null"
  }},

  "summary": {{
    "chief_complaint": "Main reason for visit in 1 sentence",
    "history": "Relevant past medical history in 1-2 sentences",
    "examination": "Key physical examination findings",
    "diagnosis": "Primary and secondary diagnoses in 1-2 sentences",
    "treatment": "Current treatment plan in 1-2 sentences",
    "recommendations": "Follow-up and recommendations",
    "one_line_summary": "Single most important clinical sentence a doctor needs to read first"
  }},

  "lab_analysis": {{
    "findings": [
      {{
        "parameter": "Test name (e.g. Glucose, Hemoglobin)",
        "value": 0.0,
        "unit": "mg/dL",
        "normal_range": "70 - 99",
        "status": "Normal / Mild / Moderate / Critical",
        "emoji": "🟢 / 🟡 / 🟠 / 🔴",
        "flag": "HIGH / LOW / NORMAL"
      }}
    ],
    "overall_severity": "Normal / Mild / Moderate / Critical",
    "overall_emoji": "🟢 / 🟡 / 🟠 / 🔴",
    "critical_count": 0,
    "moderate_count": 0,
    "mild_count": 0,
    "normal_count": 0,
    "alerts": [
      "⚠️ CRITICAL: Glucose = 285 mg/dL — far above normal range of 70-99"
    ],
    "requires_immediate_attention": false
  }},

  "risk_assessment": {{
    "readmission_risk_percent": 0,
    "complication_risk_percent": 0,
    "overall_risk_level": "Low / Medium / High / Very High",
    "risk_emoji": "🟢 / 🟡 / 🟠 / 🔴",
    "appointment_priority": "NORMAL / MEDIUM / HIGH / URGENT",
    "priority_color": "green / yellow / orange / red",
    "priority_message": "e.g. Move to earliest available slot",
    "key_risk_factors": [
      "Age > 65",
      "Uncontrolled diabetes",
      "Previous cardiac event"
    ],
    "requires_alert": false
  }},

  "bed_management": {{
    "recommended_ward": "ICU / General Ward / Emergency / Outpatient",
    "estimated_stay_days": 0,
    "discharge_note": "Brief discharge planning note"
  }},

  "doctor_advice": "2-3 sentences of specific, actionable clinical advice for the treating doctor based on the most critical findings in this report."
}}"""


def build_summary_only_prompt(report_text: str) -> str:
    return f"""You are QuickCare AI. Extract a clean patient summary from this medical report.
Return ONLY valid JSON, no markdown, no explanation.

REPORT:
\"\"\"
{report_text[:5000]}
\"\"\"

Return:
{{
  "patient_info": {{
    "name": "string",
    "age": null,
    "gender": "string"
  }},
  "chief_complaint": "string",
  "history": "string",
  "examination": "string",
  "diagnosis": "string",
  "treatment": "string",
  "recommendations": "string",
  "one_line_summary": "string"
}}"""

