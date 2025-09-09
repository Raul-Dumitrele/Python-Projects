# Image Watermarking Script

This Python script allows you to **automatically add a watermark** to all images in a folder. The watermark is positioned at the **bottom-right corner** of each image and resized proportionally.

---

## Features

- Works with `.png` and `.jpg` images.
- Automatically resizes watermark to 8% of the image width.
- Preserves transparency if the watermark is a PNG with alpha channel.
- Saves output images in a separate `output` folder.
- Supports RGB and paletted (`P`) images.

---

## Requirements

- Python 3.6+
- [Pillow](https://pillow.readthedocs.io/en/stable/) library

Install dependencies using:

```bash
pip install Pillow
```

---

## Usage

1. Put all images you want to watermark in a folder.
2. Place your watermark image (PNG or JPG) somewhere accessible.
3. Run the script:

```bash
python Image_watermark.py
```

4. Enter the folder path containing your images.
5. Enter the path to the watermark image.

6. The script will create an `output` folder and save the watermarked images there.

---

## Example

```
Enter Folder Path: C:\Users\Username\Pictures\MyPhotos
Enter Watermark Path: C:\Users\Username\Pictures\watermark.png
```

- Original folder: `input.png`
- Watermarked image saved in: `output/input.png`

---

## Notes

- The script **excludes the watermark file** itself from processing.
- Watermark is always placed **20px from the bottom-right corner**.
- For best results, use a watermark with transparency (PNG).

---

## License

This script is free to use and modify.

## Authon Name:

[Raul Dumitrele](https://github.com/Raul-Dumitrele)
