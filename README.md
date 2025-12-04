# Story Generator

A desktop application that generates creative stories using AI. Choose from various genres, set your desired word count, and get unique stories with proper formatting including bold text, italics, and paragraph breaks.

![Story Generator Screenshot](screenshot.png)

## Features

- 30+ story genres including Horror, Fantasy, Science Fiction, Romance, Fables, Nursery Rhymes, and more
- Adjustable word count (100-1000 words)
- Stories formatted with **bold** emphasis and *italic* text for thoughts/sounds
- Proper paragraph breaks for easy reading
- Save generated stories as Markdown files
- Dark-themed modern UI

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

Groq offers free access to powerful language models with generous rate limits, perfect for this story generator.

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
   pip install customtkinter requests
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
4. Adjust the word count slider
5. Click "Generate Story"
6. Optionally save the story as a Markdown file

## Files

- `main.pyw` - Main application file
- `api_key.json` - Store your Groq API key here
- `README.md` - This file
- `screenshot.png` - Application screenshot

## Technologies Used

- **customtkinter** - Modern UI framework for Python
- **Groq API** - Fast, free AI inference using Llama 3.3 70B model
- **Python 3** - Core programming language

## License

Free to use and modify for personal projects.
