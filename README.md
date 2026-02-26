# 🚀 FastAPI Project

## Setup & Run

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# Windows
source .venv/Scripts/activate
# Linux / macOS
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run development server
fastapi dev app.py


Here is a **single, clean, copy-paste–ready README.md**.
Just select all and paste into your GitHub `README.md`.

---

```md
# 🏥 Medical Report Analysing Agent API

An **AI-powered medical report analysis system** that enables:

- 💬 Medical question answering via chat
- 📄 AI-based medical report analysis (PDF)
- 🧠 Patient info extraction & lab interpretation
- 🚨 Risk assessment & clinical summaries

---

## 🌐 Base URL

```

[https://medical-report-analysing-agent.onrender.com](https://medical-report-analysing-agent.onrender.com)

```

---

## 🔹 1. Medical Chat Agent

Ask health-related or medical questions and receive AI-generated answers.

### 📌 Endpoint

```

GET /agent/chat

````

### 🧾 Query Parameters

| Parameter | Type   | Required | Description |
|---------|--------|----------|-------------|
| message | string | ✅ Yes   | Medical question |

---

### 🔧 Example Request (cURL)

```bash
curl -X GET \
'https://medical-report-analysing-agent.onrender.com/agent/chat?message=what%20is%20diabetes' \
-H 'accept: application/json'
````

---

### 📥 Example Response

```json
{
  "question": "what is diabetes",
  "response": {
    "answer": "Diabetes mellitus is a chronic metabolic disease characterized by elevated blood glucose (hyperglycemia) resulting from defects in insulin secretion, insulin action, or both. This sustained hyperglycemia leads to long-term damage, dysfunction, and failure of various organs, particularly the eyes, kidneys, nerves, heart, and blood vessels."
  }
}
```

---

### ✅ Use Cases

* Medical chatbots
* Patient education platforms
* Pre-consultation assistants
* Health awareness tools

---

## 🔹 2. Full Medical Report Analysis

Upload a medical report (PDF) and receive a detailed AI-generated clinical analysis.

### 📌 Endpoint

```
POST /report/full-analysis
```

---

### 📂 Request Type

```
multipart/form-data
```

---

### 🧾 Form Data Parameters

| Field           | Type   | Required   | Description         |
| --------------- | ------ | ---------- | ------------------- |
| file            | PDF    | ✅ Yes      | Medical report file |
| age             | number | ❌ Optional | Patient age         |
| gender          | string | ❌ Optional | Patient gender      |
| prev_admissions | number | ❌ Optional | Previous admissions |

---

### 🔧 Example Request (cURL)

```bash
curl -X POST \
'https://medical-report-analysing-agent.onrender.com/report/full-analysis' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'file=@187818665_Report_F2025-01-11T153900.pdf;type=application/pdf' \
-F 'age=0' \
-F 'gender=string' \
-F 'prev_admissions=0'
```

---

### 📥 Example Response

```json
{
  "request_id": "7fa5b4d1-877d-41c9-99fd-a11bbb48da9a",
  "filename": "187818665_Report_F2025-01-11T153900.pdf",
  "status": "success",
  "analysis": {
    "patient_info": {
      "name": "Mr. SUNDER LAL",
      "age": 70,
      "gender": "Male",
      "patient_id": "187818665"
    },
    "summary": {
      "one_line_summary": "Patient's lab results for Uric Acid and Fasting Glucose are within normal limits."
    },
    "lab_analysis": {
      "overall_severity": "Normal",
      "overall_emoji": "🟢",
      "normal_count": 2,
      "requires_immediate_attention": false
    },
    "risk_assessment": {
      "overall_risk_level": "Low",
      "risk_emoji": "🟢",
      "priority_message": "No immediate concerns based on lab results."
    },
    "bed_management": {
      "recommended_ward": "Outpatient",
      "estimated_stay_days": 0
    },
    "doctor_advice": "The patient's Uric Acid and Fasting Glucose levels are within normal reference ranges."
  }
}
```

---

## 🧠 Key Features

* 🧪 Lab value interpretation with emojis
* 📊 Risk & severity classification
* 👨‍⚕️ AI-generated doctor advice
* 🏥 Bed & ward recommendations

---

## 🚀 Ideal For

* Hospitals & clinics
* Health-tech startups
* EMR / EHR systems
* Hackathons & demos

---

## ⚠️ Disclaimer

> This API is intended for **informational and clinical decision-support purposes only**.
> It does **not replace professional medical advice or diagnosis**.

---

## 🧑‍💻 Author

Built with ❤️ for intelligent healthcare automation

```

---

If you want, next I can:
- Add **Swagger / OpenAPI docs**
- Generate **Postman collection**
- Write **frontend integration (React / Flutter)**
- Make it **hackathon-winning premium README**

Just say 🚀
```
