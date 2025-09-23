# ✊🖐✌ Rock-Paper-Scissors Game

![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Status](https://img.shields.io/badge/status-stable-success)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

> A simple **Rock-Paper-Scissors** game in Python where you play against the computer.

---

## 🚀 How to Use

### 1️⃣ Clone the project

```bash
git clone https://github.com/USER/Rock-Paper-Scissors.git
cd Rock-Paper-Scissors
```

### 2️⃣ Run the game

```bash
python rps.py
```

### 3️⃣ Instructions

- Enter the number of rounds you want to play.
- For each round, type:
  - `R` or any word starting with **R** → Rock
  - `P` or any word starting with **P** → Paper
  - `S` or any word starting with **S** → Scissors
- The program normalizes the input and compares it with the computer’s choice.

---

## 🏗️ How it Works

- Uses `random.choice()` to select Rock, Paper, or Scissors for the computer.
- Normalizes user input, so you can type `r`, `rock`, or any text starting with **R**.
- Compares the user’s choice with the computer’s and updates the score:
  - **User wins** → user score increases
  - **Computer wins** → computer score increases
  - **Tie** → score remains unchanged
- At the end, displays the overall winner.

---

## 📂 Project Structure

```
Rock-Paper-Scissors/
├── rps.py        # Main script
└── README.md     # This file
```

---

## ✍️ Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)
