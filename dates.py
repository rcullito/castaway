from datetime import datetime
from datetime import date

today = datetime.now()

print("The current date and time is", today)

# just the time

t = datetime.time(datetime.now())

print("The current time is", t)

print("The current date is", date.today())


# open the file, date, and append the time
# only ever append