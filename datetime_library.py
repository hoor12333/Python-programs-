import datetime

# Current date and time
now = datetime.datetime.now()
print("Now:", now)

# Only date
today = datetime.date.today()
print("Today:", today)

# Custom formatting
print("Formatted date:", now.strftime("%d-%m-%Y %H:%M:%S"))

# Date difference (age calculator)
birthday = datetime.date(2000, 1, 1)
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
print("Age (if born on 01-01-2000):", age)
