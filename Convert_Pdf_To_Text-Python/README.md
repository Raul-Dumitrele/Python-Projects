# 📄 PDF to Text Converter (Python + PyPDF2)

This is a **Python script** that extracts text from a `.pdf` file and saves it into a `.txt` file.  
It can either store the output in a user-specified location or automatically place it in a `temp` folder.

---

## 🔹 Features

- Converts PDF pages into plain text.
- Can save output in a custom file path or in a default `temp/` folder.
- Handles multi-page PDFs by iterating through all pages.
- Prints extracted text to the terminal while writing to file.

---

## 🔹 Requirements

- Python 3.6 or newer
- [PyPDF2](https://pypi.org/project/PyPDF2/)

Install dependencies:

```bash
pip install PyPDF2
```

---

## 🔹 Usage

1. Save the script as `pdf_to_text.py`.
2. Run it from terminal:

```bash
python Convert_Pdf_To_Text-Python.py
```

3. The script will ask for:

   - Path to the PDF file
   - Path to the output `.txt` file

   If no output path is given, the script will create a `temp/` folder and save the text there.

---

## 🔹 Example

Input:

📄 `document.pdf`

Output:

📝 `document.txt`

---

## 🔹 How It Works

1. Checks if a `temp/` folder exists, creates one if missing.
2. Takes input paths for PDF and TXT files.
3. If no TXT path provided, auto-generates one in `temp/`.
4. Reads the PDF using `PdfFileReader()`.
5. Iterates through each page with `getPage()`.
6. Extracts text with `.extractText()` and appends it to the TXT file.
7. Prints extracted content to the console.

---

## 🔹 Possible Improvements

- Use `pdfplumber` for more accurate text extraction.
- Add support for batch PDF processing.
- Handle encrypted PDFs with password prompts.
- Add command-line arguments for automation.

---

## 🔹 Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)

---
