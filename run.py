#!/usr/bin/env python3
"""
=====================================================================
ONLINE SMART FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM
BCA Minor Project Launcher
=====================================================================
"""
import os
import sys
import webbrowser
import threading
import time
import uvicorn

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(CURRENT_DIR, "backend")

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

def open_browser():
    time.sleep(1.5)
    url = "http://127.0.0.1:8000"
    
    # Try launching in dedicated Desktop App Mode (frameless window without URL bar)
    browser_candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]

    import subprocess
    for browser in browser_candidates:
        if os.path.exists(browser):
            try:
                subprocess.Popen([
                    browser,
                    f"--app={url}",
                    "--window-size=1300,850",
                    "--window-position=50,50"
                ])
                print(f"[+] Launched in Desktop App Mode using {os.path.basename(browser)}: {url}")
                return
            except Exception:
                pass

    print(f"\n Launching web interface in browser: {url} ...")
    webbrowser.open(url)

def main():
    print("=" * 70)
    print("  ONLINE SMART FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM")
    print("  College Minor Project (BCA 5th Semester)")
    print("  Stack: Python, FastAPI, OpenCV, MySQL, Bootstrap 5, Chart.js")
    print("=" * 70)
    print("\n[+] Starting FastAPI Web Server at: http://127.0.0.1:8000")
    print("[+] API Documentation at: http://127.0.0.1:8000/docs")
    print("[+] Default Admin Login: admin / admin123")
    print("[+] Default Student Login: BCA2026001 / student123\n")

    threading.Thread(target=open_browser, daemon=True).start()

    os.chdir(BACKEND_DIR)
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)

if __name__ == "__main__":
    main()
