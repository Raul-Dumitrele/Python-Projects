# ⏰ Alarm Clock (Python + Tkinter)

This is a simple **desktop alarm clock application** built with **Python** and **Tkinter**.  
It allows the user to set a specific time (hour, minute, second), and when that time is reached, a sound plays to notify the user.

---

## 🔹 Features

- **Graphical User Interface** built with Tkinter.
- **Dropdown menus** for selecting hour, minute, and second.
- Runs the alarm in a **separate thread** so the interface stays responsive.
- Plays a sound file (`sound.wav`) when the alarm time is reached.

---

## 🔹 Requirements

- Python 3.6 or newer
- Windows OS (uses `winsound` module)
- `sound.wav` file present in the same directory as the script

Install dependencies (only Tkinter is required, already included with most Python installations):

```bash
pip install tk
```

---

## 🔹 Usage

1. Place the script and `sound.wav` in the same folder.
2. Run the program:

```bash
python alarm_clock.py
```

3. Select the hour, minute, and second from the dropdown menus.
4. Click **Set Alarm**.
5. When the time matches the current system time, the sound will play.

---

## 🔹 Example Screenshot

_(You can add a screenshot of your program running here if you want.)_

---

## 🔹 How It Works

- The program uses **Tkinter** to display the interface.
- A separate **thread** is started when you press **Set Alarm** so that the GUI doesn't freeze while waiting for the alarm time.
- Every second, the program checks the current time. When it matches the set time, it plays the `sound.wav` file asynchronously.

---

## 🔹 Authon Name:

[Raul Dumitrele](https://github.com/Raul-Dumitrele)
