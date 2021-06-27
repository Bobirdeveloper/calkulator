import calendar



c = calendar.HTMLCalendar(calendar.MONDAY)
s = c.formatmonth(2021, 5)
print(s)
for month in calendar.month_name:
    print(month)

