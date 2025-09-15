
# ⏳ Countdown Timer (Python)

This is a **simple command-line countdown timer** implemented in Python.  
It takes user input (in seconds) and displays a live countdown until it reaches zero.

---

## 🔹 Features

- Displays countdown in **MM:SS format**
- Updates the timer **in place** (on the same line)
- Prints a message when the timer completes

---

## 🔹 Requirements

- Python 3.6+ (no extra dependencies required)

---

## 🔹 Usage

Run the script:

```bash
python countdown_timer.py
```

Enter the number of seconds you want to count down.  
Example run:

```text
Enter the time in seconds: 10
00:10
00:09
...
00:01
Timer Completed!
```

---

## 🔹 How It Works

- Uses `divmod()` to convert total seconds into minutes and seconds.
- Displays the countdown in `MM:SS` format.
- Updates the same line using `end="\r"` so the timer does not print multiple lines.
- Uses `time.sleep(1)` to wait for one second between updates.

---

## 🔹 Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)
