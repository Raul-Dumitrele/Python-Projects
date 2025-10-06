
# 🔋 Low Battery Notifier (Python)


![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Status](https://img.shields.io/badge/status-stable-success)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

This is a **simple Python script** that checks your laptop's battery percentage and notifies you if it drops below a certain threshold (30% by default).  
It is especially useful to avoid sudden shutdowns when running on battery.

---

## 🔹 Features

- Monitors **battery percentage** in real-time.
- Detects whether the laptop is **plugged in or not**.
- Displays a **desktop notification** when battery is low.

---

## 🔹 Requirements

Install the required dependencies:

```bash
pip install psutil py-notifier win10toast
```

- **psutil** → retrieves battery status.
- **py-notifier** + **win10toast** → display Windows desktop notifications.

> ⚠️ Works best on **Windows OS**.

---

## 🔹 Usage

Run the script from the terminal:

```bash
python battery_notifier.py
```

If your battery is below 30% and the charger is not plugged in, you will receive a notification:

**Example Notification:**  
🔔 **Low Battery — 25% remaining!!**

---

## 🔹 Customization

You can change the battery threshold by modifying this line:

```python
if percent <= 30 and plugged != True:
```

For example, use `20` if you only want notifications when battery drops below 20%.

---

## 🔹 Author

[Raul Dumitrele](https://github.com/Raul-Dumitrele)
