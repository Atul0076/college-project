#!/usr/bin/env python3
"""
EduCore Pro Manual - HTML to PDF Converter
Generates a professional PDF manual from HTML
"""

import os
import sys
import subprocess
from pathlib import Path

def create_pdf_from_html():
    """Create PDF from HTML using available system tools"""
    
    script_dir = Path(__file__).parent
    html_file = script_dir / "manual.html"
    pdf_file = script_dir / "EduCore_Pro_Manual.pdf"
    
    if not html_file.exists():
        print(f"Error: {html_file} not found!")
        return False
    
    # Try method 1: Using wkhtmltopdf
    try:
        result = subprocess.run(
            ['wkhtmltopdf', str(html_file), str(pdf_file)],
            capture_output=True,
            timeout=30
        )
        if result.returncode == 0 and pdf_file.exists():
            print(f"✓ PDF created successfully: {pdf_file}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    # Try method 2: Using Chrome/Chromium headless
    try:
        result = subprocess.run(
            ['chromium-browser', '--headless', '--disable-gpu', 
             f'--print-to-pdf={pdf_file}', f'file://{html_file}'],
            capture_output=True,
            timeout=30
        )
        if result.returncode == 0 and pdf_file.exists():
            print(f"✓ PDF created successfully: {pdf_file}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    # Try method 3: Using google-chrome
    try:
        result = subprocess.run(
            ['google-chrome', '--headless', '--disable-gpu',
             f'--print-to-pdf={pdf_file}', f'file://{html_file}'],
            capture_output=True,
            timeout=30
        )
        if result.returncode == 0 and pdf_file.exists():
            print(f"✓ PDF created successfully: {pdf_file}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    # Try method 4: Using firefox
    try:
        result = subprocess.run(
            ['firefox', '--headless', f'--print-to-file={pdf_file}', f'file://{html_file}'],
            capture_output=True,
            timeout=30
        )
        if result.returncode == 0 and pdf_file.exists():
            print(f"✓ PDF created successfully: {pdf_file}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    print("\n⚠ Note: Automatic PDF generation requires additional tools.")
    print("Available options to create PDF:\n")
    print("1. Manual Method (Recommended):")
    print("   - Open manual.html in your browser")
    print("   - Press Ctrl+P (Windows/Linux) or Cmd+P (Mac)")
    print("   - Select 'Save as PDF'")
    print("   - Save as 'EduCore_Pro_Manual.pdf'\n")
    print("2. Command Line (if tools are installed):")
    print("   - Install: wkhtmltopdf, puppeteer, or use browser headless")
    print("   - Run: wkhtmltopdf manual.html EduCore_Pro_Manual.pdf")
    
    return False

if __name__ == "__main__":
    print("=" * 60)
    print("EduCore Pro Manual - PDF Generator")
    print("=" * 60)
    
    success = create_pdf_from_html()
    
    print("\n" + "=" * 60)
    if not success:
        print("Manual (manual.html) is ready for download and printing.")
    sys.exit(0 if success else 1)
