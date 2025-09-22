# 🖥️ Shutdown & Restart Script

![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Status](https://img.shields.io/badge/status-stable-success)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

> Script simplu în Python pentru **oprirea** sau **repornirea** computerului, compatibil cu Windows, Linux și macOS.

---

## ⚠️ Atenție!

Acest script chiar va închide sau reporni calculatorul tău atunci când îl rulezi.  
Folosește-l doar în scopuri de testare / administrare și **nu-l rula din greșeală**.

---

## 🚀 Cum se folosește

### 1️⃣ Clonează proiectul

```bash
git clone https://github.com/USER/Shutdown-Restart.git
cd Shutdown-Restart
```

### 2️⃣ Rulează scriptul

```bash
python shutdown_restart.py
```

### 3️⃣ Alege acțiunea

- `r` → repornește computerul
- `s` → oprește computerul
- altă tastă → afișează mesajul "Wrong letter" și nu face nimic

---

## 🏗️ Cum funcționează

- Detectează sistemul de operare folosind `platform.system()`
- Rulează comenzile native:
  - **Windows** → `shutdown -s` / `shutdown -t 0 -r -f`
  - **Linux/macOS** → `shutdown -h now` / `reboot now`
- Dacă OS-ul nu este recunoscut → afișează un mesaj de eroare

---

## 📂 Structura proiectului

```
Shutdown-Restart/
├── shutdown_restart.py   # Scriptul principal
└── README.md             # Acest fișier
```

---

## Authon Name:

[Raul Dumitrele](https://github.com/Raul-Dumitrele)
