# 🔍 String Search in Multiple Files (Python)

![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Status](https://img.shields.io/badge/status-stable-success)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

> A simple Python script to **search for a text string in all files** within a specified directory and its subdirectories.

---

## 🚀 How to Use

### 1️⃣ Clone the project

```bash
git clone https://github.com/Raul-Dumitrele/Python-Projects.git
cd Python-Projects/String_search_from_multiple_files-Python
```

### 2️⃣ Run the script

```bash
python String_search_from_multiple_files-Python.py
```

### 3️⃣ Instructions

- Input the text string you want to search for.  
- Input the path to the directory where you want to search.  
- The script will scan all files in the directory and its subdirectories and print the paths of the files where the text is found.  
- If the text is not found, it will display a message stating so.

---

## 🏗️ How it Works

- Uses `os.walk()` to recursively traverse all folders and subfolders.  
- Opens each file (ignoring binary or unreadable files) and checks if the input text exists.  
- Prints the full path of each file containing the text.  
- If no files contain the text, prints a "not found" message.

---

## 📂 Project Structure

```
Python-Projects/
├── String_search_from_multiple_files-Python/
│   ├── String_search_from_multiple_files-Python.py   # Main script
│   └── README.md                                     # This file
```

---

## ✍️ Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)
