import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())

dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(oct21st)
print(oct21st - aboutThirtyYears)
print(oct21st - (2 * aboutThirtyYears))

# Formatting datetime to string
oct21st = datetime.datetime(2017, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))

# Parsing string to datetime
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("October of '15", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))
