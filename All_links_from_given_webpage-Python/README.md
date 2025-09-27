# 🌐 All_links_from_given_webpage-Python

![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Status](https://img.shields.io/badge/status-stable-success)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

> A Python script that extracts all links from a given webpage.

This is a simple **Python script** that extracts all hyperlinks (`<a href="...">`) from a given web page  
and saves the **first 10 links** into a text file.

---

## 🔹 Features

- Accepts a link from the user (with or without `https://`).
- Automatically adds `https://` if missing.
- Uses **requests** to fetch the page content.
- Parses the HTML with **BeautifulSoup**.
- Extracts all `<a>` tags and saves the first 10 links in a file named `MyLinks.txt`.

---

## 🔹 Requirements

- Python 3.6 or newer
- Install the dependencies with:

```bash
pip install requests beautifulsoup4
```

---

## 🔹 Usage

1. Clone or download the project.
2. Run the script:

```bash
python All_links_from_given_webpage-Python.py
```

3. Enter a website link when prompted.
4. Check the file `MyLinks.txt` to see the first 10 extracted links.

---

## 🔹 How It Works

- **requests.get(url)** fetches the page.
- **BeautifulSoup** parses the HTML code.
- Loops through all `<a>` elements and extracts the `href` attribute.
- Writes the first 10 results to `MyLinks.txt` (append mode).

---

## 🔹 Possible Improvements

- Handle invalid or unreachable URLs with `try/except`.
- Remove duplicate links before saving.
- Save all links in a CSV or JSON format for easier processing.
- Optionally display links in the console instead of only writing to file.

---

## 🔹 Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)

---
