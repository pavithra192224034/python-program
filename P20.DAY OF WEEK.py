def dayOfTheWeek(d, m, y):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    from datetime import datetime
    return days[datetime(y, m, d).weekday()]

date=int(input("Enter the date:"))
month=int(input("Enter the month:"))
year=int(input("Enter the year:"))
print(dayOfTheWeek(date,month,year))
