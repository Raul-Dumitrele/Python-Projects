# 📌 Age Calculator (Python Project)

This is a simple **Python project** that calculates a user's age in
**years, months, and days** based on their birth date. It demonstrates
handling of dates, leap years, and basic input/output in Python.

---

## 🔹 Features

- Accepts user **name, age, and birth date** as input.
- Calculates age in:
  - **Years**
  - **Months**
  - **Days**
- Handles **leap years** accurately.
- Uses Python's built-in **time** and **calendar** libraries.

---

## 🔹 Requirements

- Python 3.6 or newer

No external libraries are required.

---

## 🔹 Usage

1.  Save the script as `age_calculator.py`
2.  Run the script:

```bash
python Calculate_age-Python.py
```

3.  Enter your details when prompted (name, age, birth month, and day).
4.  The program outputs your age in years, months, and days.

---

## 🔹 Source Code

```python
# -*- coding: utf-8 -*-
import time
from calendar import isleap

def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28

name = input("Name: ")
age = input("Age: ")
birth_month = int(input("Birth month (1-12): "))
birth_day = int(input("Birth day: "))

localtime = time.localtime(time.time())

year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

for y in range(begin_year, end_year):
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

day = day + localtime.tm_mday

leap_birth = judge_leap_year(begin_year)
for m in range(1, birth_month):
    day -= month_days(m, leap_birth)
day -= (birth_day - 1)

print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
```
