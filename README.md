# 🛡️ DevSecOps CI/CD Security Demo

This project simulates a basic DevSecOps pipeline with integrated security checks using GitHub Actions, Semgrep (SAST), and OWASP Dependency-Check (SCA). It's designed to demonstrate foundational skills in secure development pipelines — especially for entry-level security roles or junior DevSecOps/ AppSec engineers.

## 🧩 Tools Used
- **GitHub Actions**: Automate security scans on every push/PR
- **Semgrep**: Static code analysis for detecting vulnerable code patterns (OWASP Top 10)
- **OWASP Dependency-Check**: Find known vulnerable dependencies
- **Sample App**: A deliberately vulnerable Python web app for security testing

## 🚀 What This Repo Shows
- Setting up a secure CI/CD pipeline from scratch
- Automating code security scans in GitHub Actions
- Interpreting SAST/SCA findings and documenting risks
- Practicing lightweight threat modeling for deployed features
- Clean pipeline execution with real-time SAST/SCA results

## 📁 Repo Structure
```
.github/workflows/
  - security.yml              <-- GitHub Actions pipeline
/src/
  - app.py                    <-- Sample vulnerable code
/threat-model/
  - stride_model.md           <-- STRIDE threat analysis
/reports/
  - semgrep_results.json      <-- Sample static analysis report
  - dependency-check-report.html  <-- Sample dependency vulnerability report
```

## 📘 How to Use This Repo
1. Clone the repository
2. Review the `app.py` for intentionally vulnerable code
3. Check the `security.yml` pipeline under `.github/workflows/`
4. Explore the `reports/` folder for sample scan results
5. Read the `threat-model/stride_model.md` to understand STRIDE analysis

## 🧠 Project Goals
- Show an understanding of secure development lifecycle (SDLC)
- Practice integrating and interpreting results from AppSec tools
- Document basic STRIDE threat modeling approach
- Build a simple but real DevSecOps workflow for job readiness

## 🙌 Inspired By
- TryHackMe DevSecOps rooms
- OWASP Top 10
- Prep for early-career security engineer roles

Made by **Anthony Whorton**
