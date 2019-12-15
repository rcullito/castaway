# mishmosh of the other files
# this may end up being the useful one
from datetime import datetime
from datetime import date

todays_date = str(date.today()) + ".txt"

#TODO spoof this with a date we don't already
# have to see how it will fail
f = open(todays_date, "a")
f.write("Somewhere between jazz and opera ")
f.close()




