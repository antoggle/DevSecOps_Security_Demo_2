# 🧠 Threat Model – DevSecOps Demo App (STRIDE)

This document presents a basic threat model for the sample Python web application (`app.py`) used in the DevSecOps Security Demo. The model uses the STRIDE methodology to identify and categorize potential security threats.

---

## 📦 Application Overview

- Framework: Flask (Python)
- Key Features:
  - `/greet`: Greets a user by name
  - `/search`: Performs a SQL query on user input
  - `/run`: Executes OS commands based on input

---

## 🔐 STRIDE Threat Categories

| Threat Type | Description | Example in App |
|-------------|-------------|----------------|
| **Spoofing** | Forging identity | No login or auth, attacker can spoof any user |
| **Tampering** | Modifying data | Direct input to SQL query, attacker could change query behavior |
| **Repudiation** | Denying actions | No logging or tracking; attacker actions are untraceable |
| **Information Disclosure** | Exposing data | SQL error messages may reveal schema; `/run` might output sensitive system info |
| **Denial of Service** | Crashing or overloading service | Repeated `/run?cmd=...` calls could exhaust server resources |
| **Elevation of Privilege** | Gaining unauthorized access | `/run` allows execution of arbitrary commands, potentially allowing privilege escalation |

---

## 🛡️ Mitigation Recommendations

- Use input validation/sanitization libraries (e.g., parameterized SQL)
- Implement authentication and session controls
- Log all incoming requests and user actions
- Disable or restrict use of `os.popen()` in production
- Limit input length and rate-limit API endpoints

---

## 🧭 Tools Used

- [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) for diagramming (not included here)
- Manual STRIDE walkthrough

---

Prepared by: **Anthony Whorton**  
