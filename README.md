# EDI Inspector

A simple graphical tool to inspect and validate EDI files (EDIFACT format).  
It highlights common structural issues, starting with BGM segment verification.

---

## 🎯 Features

- Open EDI files (`.txt`, `.edi`, etc.) via a file dialog
- Display EDI content in a scrollable text area
- Highlight lines with structural issues in red (e.g. incomplete BGM segment)
- Easy to extend with new validation rules

---

## 🖥️ Interface Preview

Basic Tkinter interface with a button to open EDI files and a live viewer.

---

## 🧪 How to Run

Make sure you have Python 3 installed.

```bash
git clone https://github.com/<your-username>/edi-inspector.git
cd edi-inspector
python main.py
