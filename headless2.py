from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime
import pandas as pd
import vt 

with open("virustotal_api_key.txt", "r") as f:
    VT_API_KEY = f.read().strip()

client = vt.Client(VT_API_KEY)
excel_file = "urls.xlsx"
data = pd.read_excel(excel_file)
urls = data['URLs'].dropna().apply(lambda u: u if u.startswith("http") else f"http://{u}").tolist()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu") 
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
chrome_options.add_argument("--disk-cache-dir=/tmp/chrome-cache") 
chrome_options.add_argument("--window-size=1920x1080") 
chrome_options.binary_location = "/snap/bin/chromium"

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

def create_folder(url):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    folder_name = f"{timestamp}_{url.replace('https://', '').replace('http://', '').replace('/', '_')}"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

def process_virustotal(url, folder_path):
    try:
        print(f"Submitting URL to VirusTotal: {url}")
        url_id = vt.url_id(url) 
        client.scan_url(url)
        vt_gui_url = f"https://www.virustotal.com/gui/url/{url_id}/detection"
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        vt_screenshot_path = os.path.join(folder_path, f"{timestamp}_virustotal_screenshot.png")
        print("Opening VirusTotal results page in headless Chromium...")
        driver.get(vt_gui_url)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        driver.save_screenshot(vt_screenshot_path)
        print(f"VirusTotal screenshot saved: {vt_screenshot_path}")

    except Exception as e:
        print(f"Error processing URL in VirusTotal: {e}")

for url in urls:
    try:
        print(f"Processing URL: {url}")
        folder_path = create_folder(url)
        process_virustotal(url, folder_path)
        print(f"Opening website in headless Chromium: {url}")
        driver.get(url)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        website_screenshot_path = os.path.join(folder_path, f"{timestamp}_website_screenshot.png")
        driver.save_screenshot(website_screenshot_path)
        print(f"Website screenshot saved: {website_screenshot_path}")

    except Exception as e:
        print(f"Error processing {url}: {e}")

driver.quit()
client.close()
