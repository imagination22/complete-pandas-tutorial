year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

import calendar

calendar = calendar.monthcalendar(year, month)
if not calendar:
    print("Invalid month or year.")
else:
    print(calendar)
