# Threat Intelligence and Reconnaissance Automation Tool

## Overview
This project is an automation tool designed for **threat intelligence gathering** and **adversary emulation**. It automates submitting URLs to VirusTotal for analysis and captures screenshots of both the VirusTotal results and rendered websites using a headless browser. This tool enables security professionals to efficiently collect and analyze domain behavior for **reconnaissance**, **risk assessment**, and **adversary simulation**.

---

## Features
- **VirusTotal Integration**: Automatically submits URLs to VirusTotal to analyze threat intelligence scores and generate detailed reports.
- **Headless Website Rendering**: Captures rendered website screenshots for visual and structural analysis.
- **Threat Reconnaissance**: Simulates adversarial behavior to gather information on potential attack surfaces.
- **Automated Reporting**: Saves all outputs (screenshots and VirusTotal results) in a structured, timestamped format for documentation.
- **Scalable URL Processing**: Processes multiple URLs from an input file, making it suitable for bulk analysis.

---

## Use Cases
1. **Adversary Emulation**:
   - Mimics adversary reconnaissance techniques by automating URL submissions to VirusTotal.
   - Simulates phishing or exploit delivery scenarios using headless browser interactions.

2. **Threat Intelligence Gathering**:
   - Captures VirusTotal reports and visual representations of websites for insights into URL reputation and risk levels.

3. **Phishing Domain Analysis**:
   - Analyzes suspicious URLs used in phishing campaigns.
   - Validates how security defenses respond to adversarial domains.

4. **OSINT (Open Source Intelligence) Support**:
   - Performs reconnaissance on domains to evaluate their content and potential threats, aiding red team assessments.

5. **Reporting and Documentation**:
   - Provides a structured output for documenting adversarial tactics, techniques, and procedures (TTPs) during simulated attacks.

---

## Prerequisites
1. **Python 3.7 or higher**: Ensure Python is installed.
2. **ChromeDriver**: Download and place the appropriate version of ChromeDriver for your system in `/usr/local/bin`.
3. **Chromium Browser**: The script is configured to use Chromium installed via Snap (`/snap/bin/chromium`).
4. **Required Python Libraries**:
   - `selenium`
   - `pandas`
   - `vt-py` (VirusTotal API client)
   - `openpyxl`

Install them using:
```bash
pip install selenium pandas vt-py openpyxl
```

---

## Setup
### Clone the Repository:
```bash
git clone <repository-url>
cd <repository-folder>
```

### Prepare the Input File:
- Place your URLs in an Excel file named `urls.xlsx` with a column named `URLs`.

### VirusTotal API Key:
- Save your VirusTotal API key in a file named `virustotal_api_key.txt` in the project root directory.

### ChromeDriver Setup:
- Ensure the correct version of ChromeDriver is placed in `/usr/local/bin`.

---

## Usage
### Run the script:
```bash
python3 headless2.py
```

- The script processes each URL in the Excel file and:
  - Submits the URL to VirusTotal and saves a screenshot of the results page.
  - Opens the URL in a headless browser and captures a screenshot of the website.

### Output:
- For each URL, the following files are created in a timestamped folder:
  - `<timestamp>_virustotal_screenshot.png`: Screenshot of the VirusTotal results page.
  - `<timestamp>_website_screenshot.png`: Screenshot of the website.

---

## Example

### Input:
`urls.xlsx`:
| URLs              |
|-------------------|
| www.nytimes.com   |
| www.theguardian.com |

### Output:
1. **Folder**: `20241204_231334_www.nytimes.com/`
   - `20241204_231334_virustotal_screenshot.png`
   - `20241204_231334_website_screenshot.png`
2. **Folder**: `20241204_231334_www.theguardian.com/`
   - `20241204_231334_virustotal_screenshot.png`
   - `20241204_231334_website_screenshot.png`

---

## Extending the Project
1. **Integrate with Threat Intelligence Platforms (TIPs)**:
   - Automate the submission of outputs to TIPs for enhanced threat analysis.

2. **Support Malware Sandboxing**:
   - Add features to evaluate downloaded payloads in sandbox environments.

3. **Enhance OSINT Capabilities**:
   - Include features to collect metadata, subdomains, and server information.

---
