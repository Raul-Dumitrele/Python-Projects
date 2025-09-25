# 🧩 Sudoku Game (Python + Tkinter)

![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Status](https://img.shields.io/badge/status-stable-success)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

> A simple Python project to **generate, solve, and play Sudoku** using a graphical interface built with Tkinter.

---

## 🚀 How to Use

### 1️⃣ Clone the project

```bash
git clone https://github.com/Raul-Dumitrele/Python-Projects.git
cd Python-Projects/Sudoku
```

### 2️⃣ Run the script

```bash
python Sudoku.py
```

### 3️⃣ Instructions

- Click **Generate Sudoku** to create a new random puzzle.  
- Fill in the empty cells with numbers between 1–9.  
- Invalid inputs are highlighted in **red**.  
- Valid but incorrect numbers are highlighted in **yellow**.  
- Correct inputs are highlighted in **green**.  
- Use **Solve Sudoku** to automatically solve the puzzle.  
- Use **Clear Table** to reset the grid.

---

## 🏗️ How it Works

- Uses **backtracking** to generate and solve Sudoku puzzles.  
- Randomly removes numbers to create playable puzzles.  
- Validates each input in real-time.  
- Tkinter canvas is used to draw the 9x9 grid and place input fields.

---

## 📂 Project Structure

```
Python-Projects/
├── Sudoku/
│   ├── Sudoku.py     # Main script
│   └── README.md     # This file
```

---

## ✍️ Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)
