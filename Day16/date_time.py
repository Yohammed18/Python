from datetime import datetime, date

date_now = date.today()
date_time = datetime.now()
print(type(date_now),' ', date_now)
print(type(date_time),' ', date_time)

print(date_now.day)
print(date_time.day)

new_year = datetime(2024, 1, 13)
print(new_year)
print(new_year.month)


# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

# Get the current day, month, year, hour, minute and timestamp from datetime module
print("\n")
now = datetime.now()
print("Exercises: Day 16")
print(f"Day = {now.day}")
print(f"Month = {now.month}")
print(f"Year = {now.year}")
print(f"Hour = {now.hour}")
print(f"Minute = {now.minute}")
print()
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
current_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(current_date)
# Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(f"Time: {date_object}")
# Calculate the time difference between now and new year.
print()
today = date(year=2024, month=7, day=29)
new_year = date(year=2025, month=1, day=1)
# Time lest for new year
print('Time left for new year {}.'.format(new_year-today))