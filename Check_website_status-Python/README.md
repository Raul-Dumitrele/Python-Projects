# 🌐 Website Status Checker (Python Project)

This is a simple **Python script** that checks whether websites listed
in a text file are **working or not**.\
The script sends HTTP requests to each website and saves the results in
a CSV file.

---

## 🔹 Features

- Reads a list of websites from `websites.txt`.
- Sends HTTP requests to check their status.
- Marks websites as:
  - **working** → if HTTP status code is 200
  - **not working** → otherwise (404, 500, etc.)
- Saves results into `website_status.csv`.

---

## 🔹 Requirements

- Python 3.6 or newer
- Install dependencies with:

```bash
pip install requests
```

---

## 🔹 Usage

1.  Create a file named `websites.txt` with one website per line, e.g.:

```{=html}
<!-- -->
```

    https://google.com
    https://github.com
    https://thissitedoesnotexist.com

2.  Run the script:

```bash
python Check_website_status-Python.py
```

3.  The results will be saved in `website_status.csv`.

---

## 🔹 Output Example (`website_status.csv`)

```csv
Website,Status
https://google.com,working
https://github.com,working
https://thissitedoesnotexist.com,not working
```

---

## 🔹 Source Code

```python
import csv
import requests

status_dict = {"Website": "Status"}

def main():
    with open("websites.txt", "r") as fr:
        for line in fr:
            website = line.strip()
            status = requests.get(website).status_code
            status_dict[website] = "working" if status == 200 else "not working"

    with open("website_status.csv", "w", newline="") as fw:
        csv_writers = csv.writer(fw)
        for key in status_dict.keys():
            csv_writers.writerow([key, status_dict[key]])

if __name__ == "__main__":
    main()
```
