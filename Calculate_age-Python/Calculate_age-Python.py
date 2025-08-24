# -*- coding: utf-8 -*-
import time
from calendar import isleap

# judge the leap year
def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False


# returns the number of days in each month
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

localtime = time.localtime(time.time())                             #Obține data și ora curentă sub formă de structură time.struct_time.

year = int(age)                                                     #Transformă vârsta în număr întreg.
month = year * 12 + localtime.tm_mon                                #Calcul aproximativ al lunilor trăite: ani × 12 + luna curentă.
day = 0                                                             #Inițializează contorul pentru zile.

begin_year = int(localtime.tm_year) - year                          #Determină anul nașterii (begin_year) și anul curent (end_year) pe baza vârstei.
end_year = begin_year + year

# calculate the days
for y in range(begin_year, end_year):                               #Adună zilele pentru fiecare an complet trăit (de la anul nașterii până anul trecut).
    if (judge_leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)                      #Adaugă zilele lunilor trecute din anul curent.
for m in range(1, localtime.tm_mon):
    day = day + month_days(m, leap_year)

day = day + localtime.tm_mday                                       #Adaugă ziua curentă pentru a avea totalul de zile până azi.


leap_birth = judge_leap_year(begin_year)                            #Aici scazem zilele dintre 1 ianuarie și ziua reală de naștere ---
for m in range(1, birth_month):
    day -= month_days(m, leap_birth)
day -= (birth_day - 1)  # scazi zilele din luna nașterii înainte de ziua ta

print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))