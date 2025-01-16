# Threat Intelligence and Reconnaissance Automation Tool

## Overview
A cybersecurity tool for **threat intelligence gathering** and **adversary emulation**. This tool automates URL analysis with the **VirusTotal API** and headless browser automation, capturing screenshots for efficient domain reconnaissance and risk assessment.

---

## Features
- Analyze URLs using VirusTotal and save results as screenshots.
- Automate website rendering with headless browser screenshots.
- Organize outputs in timestamped folders for easy tracking.

---

## Quick Start
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Add URLs to `urls.xlsx` under a column named `URLs`.
3. Save your VirusTotal API key in `virustotal_api_key.txt`.
4. Run the script:
   ```bash
   python3 headless2.py
   ```

---

## Outputs
- Screenshots of VirusTotal results and rendered websites.

---

## Documentation
See the [Documentation](documentation.md) for detailed instructions and examples.

---
