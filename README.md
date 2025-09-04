# 🎵 Audio Converter

A **Python** script to convert audio files from any format to another format of your choice using **pydub** and **ffmpeg**.

---

## 🚀 Features

- 🎶 Supports multiple audio formats: `mp3`, `m4a`, `wav`, `flac`, `ogg`, `aac`, `wma`
- 🖥 Interactive: choose the output format **for each file individually**
- 🔍 Automatically detects all supported audio files in the folder
- 💾 Keeps the base filename intact

---

## 🛠 Requirements

- Python 3.11+
- [ffmpeg](https://ffmpeg.org/download.html) installed and path added to system environment variables
- Python library `pydub`

Install pydub in your virtual environment:

```bash
pip install pydub
🎬 How to Use

Place your audio files and AudioConverter.py in the same folder.

Open Command Prompt and navigate to the folder:
cd C:\AudioConvert
Activate your virtual environment:
venv\Scripts\activate
Run the script:
python AudioConverter.py
Follow the prompts to choose output formats for each file.
⚡ Notes

Only files with extensions mp3, m4a, wav, flac, ogg, aac, wma are detected.

Converted files will appear in the same folder.

Virtual environment (venv) and converted files are ignored via .gitignore.