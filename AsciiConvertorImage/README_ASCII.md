# 🖼️ ASCII Image Converter (Python + PIL)

This is a **Python script** that converts an image into ASCII art and saves the result in a text file.  
It works by resizing the image, calculating the brightness of each pixel, and mapping brightness levels to ASCII characters.

---

## 🔹 Features

- Opens an image and resizes it to a smaller version (based on a scale factor).
- Converts each pixel’s brightness into an ASCII character.
- Outputs a **text file** containing the ASCII art.
- Allows customization of:
  - Input image
  - Output text file name
  - Scale factor
  - Output format (PNG, JPG, etc.)

---

## 🔹 Requirements

- Python 3.6 or newer  
- [Pillow (PIL)](https://pypi.org/project/Pillow/) library  

Install dependencies:

```bash
pip install pillow
```

---

## 🔹 Usage

1. Place the image you want to convert in the same folder as the script.
2. Run the program:

```bash
python AsciiConvertorImage.py
```

3. Adjust the parameters in the `asciiConvert()` call at the bottom of the file:

```python
asciiConvert("my_image.png", "png", "output.txt", "3")
```

- **"my_image.png"** → input image file  
- **"png"** → output format for the resized image  
- **"output.txt"** → name of the output file containing ASCII art  
- **"3"** → scale factor (higher = smaller image = less detail)

4. Open the generated text file to see the ASCII art.

---

## 🔹 How It Works

1. Opens the image with `PIL.Image.open()`.
2. Resizes the image using the given scale factor.
3. Loads pixel data and calculates brightness: `brightness = sum(pix[x, y])`.
4. Maps brightness ranges to ASCII characters like `#`, `X`, `%`, `*`, `+`, `/`, etc.
5. Writes the resulting ASCII grid into a text file line by line.

---

## 🔹 Possible Improvements

- Support grayscale conversion before brightness mapping (for more accuracy).
- Allow custom character sets (e.g. user-defined brightness-to-ASCII mapping).
- Option to display ASCII art directly in the terminal.
- Option to generate colored ASCII art (ANSI escape codes).

---

## 🔹 Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)

---
