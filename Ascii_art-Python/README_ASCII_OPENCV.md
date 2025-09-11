# 🎨 Image to ASCII Converter (Python + OpenCV)

This is a **Python script** that converts an image into ASCII art using **OpenCV** and **NumPy**.  
It resizes the image, applies thresholding, maps brightness ranges to ASCII symbols, and prints the ASCII art directly to the terminal.

---

## 🔹 Features

- Converts images into ASCII art using a custom symbol set.
- Automatically resizes images so the output fits in the terminal.
- Uses brightness thresholding to determine which ASCII character to print.
- Can take an image path from the command line or use a default image.

---

## 🔹 Requirements

- Python 3.6 or newer  
- [OpenCV](https://pypi.org/project/opencv-python/)  
- [NumPy](https://pypi.org/project/numpy/)

Install dependencies:

```bash
pip install opencv-python numpy
```

---

## 🔹 Usage

1. Place the script in the same folder as the image you want to convert.
2. Run the script from the terminal:

```bash
python ascii_opencv.py my_image.png
```

If no image path is provided, the script will use **sample_image.png** by default.

---

## 🔹 Example

Input:

📷 `sample_image.png`

Output (printed in terminal):

```text
##########----****++++
######-----****++++ooo
####------****++++oooo
```

(The output will vary depending on the image.)

---

## 🔹 How It Works

1. Reads the image in **grayscale** using `cv2.imread()`.
2. Resizes the image to fit better in the terminal.
3. Applies thresholding based on predefined values `[0, 50, 100, 150, 200]`.
4. Maps brightness levels to ASCII characters from `symbols_list`.
5. Prints the ASCII art row by row to the terminal.

---

## 🔹 Possible Improvements

- Allow custom symbol sets and thresholds as arguments.
- Save ASCII output to a file instead of just printing.
- Add color ASCII art using ANSI escape codes.
- Allow interactive resizing for better visualization.

---

## 🔹 Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)

---
