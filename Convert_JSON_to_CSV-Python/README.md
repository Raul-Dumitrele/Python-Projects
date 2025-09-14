# 📑 JSON to CSV Converter (Python)

This is a **Python script** that converts a JSON file (`input.json`) into a CSV file (`output.csv`).  
It reads structured JSON data, extracts the headers, and writes the corresponding rows into a properly formatted CSV file.

---

## 🔹 Features

- Reads data from a JSON file.
- Automatically extracts headers (keys from the first JSON object).
- Converts all objects into CSV rows.
- Writes output to `output.csv`.
- Basic error handling included.

---

## 🔹 Requirements

- Python 3.6 or newer
- No external libraries required (uses only built-in `json` module).

---

## 🔹 Usage

1. Place your `input.json` file in the same folder as the script.  
   Example `input.json`:

   ```json
   [
     { "Name": "Alice", "Age": 25, "Birthyear": 1998 },
     { "Name": "Bob", "Age": 30, "Birthyear": 1993 }
   ]
   ```

2. Run the script from the terminal:

   ```bash
   python Convert_JSON_to_CSV-Python.py
   ```

3. The script will generate an `output.csv` file with the following content:
   ```csv
   Name,Age,Birthyear
   Alice,25,1998
   Bob,30,1993
   ```

---

## 🔹 How It Works

1. Opens `input.json` and loads the data with `json.loads()`.
2. Extracts the keys from the first object to use as CSV headers.
3. Iterates through each JSON object and writes rows with values.
4. Saves everything into `output.csv`.
5. Catches exceptions and prints error messages if something goes wrong.

---

## 🔹 Possible Improvements

- Use Python’s built-in `csv` module for cleaner handling of CSV formatting.
- Add command-line arguments for custom input/output file names.
- Validate JSON structure before processing.
- Handle nested JSON objects with flattening.

---

## 🔹 Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)

---
