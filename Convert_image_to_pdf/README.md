# 🖼️ Image(s) to PDF Converter (Python + img2pdf)

This is a **Python script** that converts `.jpg` images into a single `.pdf` file using **img2pdf**.  
It supports both converting a single image or batch processing all images in a folder.

---

## 🔹 Features

- Converts `.jpg` images to PDF.
- Supports both single file and entire folder input.
- Automatically skips non-image files and subdirectories.
- Outputs a single file named `output.pdf`.

---

## 🔹 Requirements

- Python 3.6 or newer
- [img2pdf](https://pypi.org/project/img2pdf/)

Install dependencies:

```bash
pip install img2pdf
```

---

## 🔹 Usage

1.Save the script as img_to_pdf.py.

2.Modify the filepath variable inside the script with your folder or image path.
Alternatively, you can pass it as a command-line argument (uncomment sys.argv[1]).

3.Run the script from terminal:

```bash
python Convert_image_to_pdf-Python.py

```

---

## 🔹 How It Works

1.Checks if filepath is a directory or a file.
2.If directory → iterates through all files and selects only .jpg images.
3.If file → processes it directly if it ends with .jpg.
4.Uses img2pdf.convert() to merge images into a single PDF.
5.Writes result to output.pdf.

---

## 🔹 Possible Improvements

- Add support for .png, .jpeg, and other formats.
- Allow custom output file names via command-line argument.
- Add recursive search through subdirectories.
- Option to generate one PDF per image instead of merging

---

## 🔹 Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)

---
