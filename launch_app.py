#!/usr/bin/env python3
"""
=====================================================================
ONLINE SMART FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM
Desktop App Mode Launcher
=====================================================================
"""
import os
import sys
import time
import socket
import threading
import subprocess
import uvicorn

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(CURRENT_DIR, "backend")

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

def is_port_in_use(port: int = 8000) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

def start_backend():
    os.chdir(BACKEND_DIR)
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="warning")

def open_desktop_app():
    url = "http://127.0.0.1:8000"
    
    # Wait until backend is responding
    for _ in range(40):
        if is_port_in_use(8000):
            break
        time.sleep(0.2)
    
    time.sleep(0.5)

    # Candidate browsers for App Mode (Window without URL bar)
    browser_candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]

    launched = False
    for browser in browser_candidates:
        if os.path.exists(browser):
            try:
                subprocess.Popen([
                    browser,
                    f"--app={url}",
                    "--window-size=1300,850",
                    "--window-position=50,50"
                ])
                launched = True
                print(f"[+] Launched in Native App Mode using: {os.path.basename(browser)}")
                break
            except Exception as e:
                continue

    if not launched:
        import webbrowser
        webbrowser.open(url)
        print("[+] Opened in default web browser.")

def main():
    print("=" * 65)
    print("  SMART FACE RECOGNITION ATTENDANCE SYSTEM - DESKTOP APP")
    print("=" * 65)

    # Start app window in separate thread
    threading.Thread(target=open_desktop_app, daemon=True).start()

    # Start backend server if not already running
    if not is_port_in_use(8000):
        print("[+] Initializing local background services...")
        start_backend()
    else:
        print("[+] Server already running on port 8000. Launching application window...")
        # Keep process alive so background thread executes
        time.sleep(3)

if __name__ == "__main__":
    main()
