# secureai-data-intelligence-platform
AI-powered platform for detecting sensitive data, security risks, and anomalies from logs with intelligent risk analysis and insights.


## Problem Statement

Modern applications generate large volumes of logs that may contain sensitive data such as passwords, API keys, tokens, and user information. These exposures can lead to serious security vulnerabilities if not detected early.

---

## Solution

This project provides an AI-powered Secure Data Intelligence Platform that:

- Scans logs for sensitive data
- Detects security issues and anomalies
- Calculates risk levels
- Generates meaningful security insights

---

## ⚙️ Features

- 📂 Log file upload (.txt, .log)
- 🔍 Sensitive data detection:
  - Emails
  - Passwords
  - API Keys
  - Tokens
  - Phone numbers
- ⚠️ Security issue detection:
  - Stack traces (errors)
  - Brute-force login attempts
- 📊 Risk Engine:
  - Risk score calculation
  - Risk level classification (Low / Medium / High)
- 🧠 AI-like Insights generation
- 🌐 Simple UI for interaction

---

## Architecture


User Input (File)

↓

Parser (Read logs)

↓

Data Scanner (Regex Detection)

↓

Log Analyzer (Pattern Detection)

↓

Risk Engine

↓

Insights Generator

↓

Output (UI + JSON)


---

## Technologies Used

- **Backend:** Python, FastAPI  
- **Frontend:** HTML, CSS, JavaScript  
- **Detection:** Regex-based pattern matching  
- **Architecture:** Modular design (Scanner, Risk Engine, Insights)

---

## How to Run

### 1. Install dependencies

pip install -r requirements.txt


### 2. Run backend

cd backend
uvicorn main:app --reload


### 3. Run frontend
- Open `frontend/index.html` using Live Server

---

## Example Output

- Detects sensitive entries from logs
- Provides risk score and level
- Generates insights like:
  - "API keys exposed in logs"
  - "Multiple failed login attempts detected"

---

## Challenges Faced

- Designing accurate regex for detecting sensitive data  
- Handling multiple log patterns  
- Creating meaningful insights without heavy AI models  
- Integrating frontend with backend (CORS issues)

---

## Future Improvements

- Real-time log monitoring  
- Advanced AI/ML-based anomaly detection  
- Data masking and blocking policies  
- Support for PDF, SQL, and chat inputs  

---

##  Author
Akshatha G Dhongadi
