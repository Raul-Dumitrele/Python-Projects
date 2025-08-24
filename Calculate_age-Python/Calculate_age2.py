from datetime import datetime

# Ask for name and birthday
name = input("Enter your name: ")
birthday_input = input("Enter your birthday (YYYY-MM-DD): ")

# Convert the input string into a datetime object
birthday = datetime.strptime(birthday_input, "%Y-%m-%d")                    #Converts the entered string into a datetime object, which allows easy calculations with the data.

# Get today's date
today = datetime.today()                                                    #Get the current date and time from the computer.

# Calculate the age difference
years = today.year - birthday.year                                          #Calculates the difference in years between the current year and the year of birth.
months = years * 12 + today.month - birthday.month                          #Converts these years to months and adds the difference in months between the current year and the year of birth.
days = (today - birthday).days  + 1                                         #Calculates the total number of days between the date of birth and today.+1 including the day of birth

# If the birthday hasn't happened yet this year, adjust the years and months
if (today.month, today.day) < (birthday.month, birthday.day):               #Check if the birthday hasn't passed yet in the current year.If it hasn't, subtract 1 from the year and 1 from the month to make it correct.

    years -= 1
    months -= 1

# Show the result
print(f"{name}'s age is {years} years, or {months} months, or {days} days.")
