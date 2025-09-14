# 🖼️ PNG to ICO Converter (Python + Tkinter)

This is a **Python desktop app** built with **Tkinter** and **Pillow**.  
It allows you to select a `.png` image and convert it into an `.ico` file through a simple graphical interface.

---

## 🔹 Features

- User-friendly GUI built with Tkinter.
- Browse and select any `.png` image from your system.
- Convert and save the image as `.ico` format.
- Error handling for missing or invalid files.
- Success confirmation popup after conversion.

---

## 🔹 Requirements

- Python 3.7 or newer
- [Pillow](https://pypi.org/project/Pillow/) (Python Imaging Library fork)

Install dependencies:

```bash
pip install pillow
```

---

## 🔹 Usage

1. Save the script as `Convert_PNG_to_ICO_UI-Python.py`.
2. Run it from terminal:

```bash
python Convert_PNG_to_ICO_UI-Python.py
```

3. A GUI window will open:
   - Click **Import PNG File** to choose an image.
   - Click **Convert PNG to ICO** to save the image in `.ico` format.

---

## 🔹 How It Works

1. Opens the file explorer with `filedialog.askopenfilename()` for PNG input.
2. Loads the image with Pillow’s `Image.open()`.
3. Prompts user to select save location with `asksaveasfilename()`.
4. Saves the converted file in `.ico` format using `img.save()`.
5. Displays error popups if no file is selected, or success popup when done.

---

## 🔹 Possible Improvements

- Add drag-and-drop functionality.
- Allow batch PNG → ICO conversions.
- Add support for resizing before conversion.
- Create a packaged `.exe` with PyInstaller for Windows users.

---

## 🔹 Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)

---
