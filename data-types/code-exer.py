# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age_as_int = int(age)
year_remaining = 90 - age_as_int
day_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
months_remaining = year_remaining * 12

# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
print(
    f"You have {day_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
