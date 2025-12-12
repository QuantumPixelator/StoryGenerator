# Story Generator

A desktop application that generates creative stories using AI. Choose from various genres, set your desired word count, and get unique stories with proper formatting.

![Story Generator Screenshot](screenshot.png)

## Prerequisites

- Python 3.8 or higher
- A free Groq API key

## Getting Your Free Groq API Key

1. Visit [https://console.groq.com/keys](https://console.groq.com/keys)
2. Sign up for a free account (no credit card required)
3. Click "Create API Key"
4. Copy your API key
5. Open `api_key.json` in this project folder
6. Replace the placeholder with your actual API key:
   ```json
   {"api_key": "your_groq_api_key_here"}
   ```

## Installation

1. Clone or download this repository
2. Create a virtual environment (recommended):
   
   **Windows (PowerShell):**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   
   **macOS/Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Groq API key to `api_key.json` (see above)

## Usage

1. Activate the virtual environment (if using one):
   
   **Windows (PowerShell):**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   
   **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

2. Run the application:
   
   **Windows:**
   ```powershell
   py main.pyw
   ```
   
   **macOS/Linux:**
   ```bash
   python3 main.pyw
   ```

3. Select a genre from the dropdown
4. Adjust the word count slider (increments of 10)
5. Click "Generate Story"
6. Optionally save the story in your preferred format (Markdown, RTF, DOCX, Text, or PDF)

## License

IDGAF License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and its documentation files ("the Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

**THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.**

**IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**

### Clear Conditions

Zero Requirement
You are granted all permissions without any conditions. You do not need to retain, reproduce, or include any copyright notice or a copy of this license when you redistribute the Software.

Total Waiver of Liability
By choosing to use, copy, or modify the Software in any way, you are agreeing to completely and permanently release the original author(s) from all liability. If anything goes wrong, you are entirely responsible.

---

**END**
