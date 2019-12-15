# mishmosh of the other files
# this may end up being the useful one
from datetime import datetime
from datetime import date

todays_date = date.today()
date_filename = str(todays_date) + ".txt"
#TODO spoof this with a date we don't already
# have to see how it will fail
f = open(date_filename, "a")

t = datetime.now()

timestamp_message = "The current time of day is " + t.strftime("%X")

f.write(timestamp_message)
f.close()




