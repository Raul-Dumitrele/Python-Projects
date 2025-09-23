# 🎬 Split Media File with FFmpeg

![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Status](https://img.shields.io/badge/status-stable-success)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

> A simple Python script that splits a media file into **two parts** using FFmpeg.  

---

## 🚀 How to Use

### 1️⃣ Clone the project

```bash
git clone https://github.com/Raul Dumitrele/SplitFile-Python.git
cd SplitFile-Python
```

### 2️⃣ Install requirements

```bash
pip install ffmpeg-python
```

⚠️ You also need **FFmpeg** installed on your system.  
[Download FFmpeg](https://ffmpeg.org/download.html)

### 3️⃣ Run the script

```bash
python split_media.py input.mp4 5 10 part1.mp4 part2.mp4
```

### 4️⃣ Arguments

- `inputfile` → the media file you want to split  
- `starttime` → start time (in seconds) for the first part  
- `endtime` → end time of the first part / start time of the second part  
- `outputfile1` → output file for the first part  
- `outputfile2` → output file for the second part  

---

## 🏗️ How it Works

- Reads arguments from the command line with **argparse**.
- Uses **ffmpeg-python** to create two video/audio streams:
  - First stream: from `starttime` to `endtime`.
  - Second stream: from `endtime` to the end of the file.
- Saves the two streams into separate output files.  

Example:  

```bash
python SplitFile-Python.py video.mp4 5 10 clip1.mp4 clip2.mp4
```

This will cut `video.mp4` into:
- `clip1.mp4` → from 5s to 10s  
- `clip2.mp4` → from 10s to the end  

---

## 📂 Project Structure

```
Split-Media-File/
├── SplitFile-Python.py   # Main script
└── README.md        # This file
```

---

## ✍️ Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)
