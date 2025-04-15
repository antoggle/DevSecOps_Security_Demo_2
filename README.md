# 🛡️ DevSecOps CI/CD Security Demo

This project simulates a basic DevSecOps pipeline with integrated security checks using GitHub Actions, Semgrep (SAST), and OWASP Dependency-Check (SCA). It's designed to demonstrate foundational skills in secure development pipelines — especially for entry-level security roles or junior DevSecOps/ AppSec engineers.

## 🧩 Tools Used
- **GitHub Actions**: Automate security scans on every push/PR
- **Semgrep**: Static code analysis for detecting vulnerable code patterns
- **OWASP Dependency-Check**: Find known vulnerable dependencies
- **Sample App**: A simple Python web app for testing the pipeline

## 🚀 What This Repo Shows
- Setting up a secure CI/CD pipeline from scratch
- Automating code security scans in GitHub Actions
- Interpreting SAST/SCA findings and documenting risks
- Practicing lightweight threat modeling for deployed features

## 📁 Repo Structure
```
/.github/workflows/
  - security.yml  <-- GitHub Actions pipeline
/src/
  - app.py        <-- Sample vulnerable code
/threat-model/
  - stride_model.md
/reports/
  - semgrep_results.json
  - dependency-check-report.html
```

## 🧠 Project Goals
- Show an understanding of secure development lifecycle (SDLC)
- Practice integrating and interpreting results from AppSec tools
- Document basic STRIDE threat modeling approach
- Build a simple but real DevSecOps workflow for job readiness

## 🙌 Inspired By
- TryHackMe DevSecOps rooms
- OWASP Top 10
- Early-career security engineer prep for roles like HashiCorp and Intellectt Inc

Made by **Anthony Whorton**
