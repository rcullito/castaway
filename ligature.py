# mishmosh of the other files
# this may end up being the useful one
from datetime import datetime
from datetime import date
from sense_hat import SenseHat

# helper fns
def pretty_sense(sensory):
    return (str(round(sensory)))

# initialize sensor
sense = SenseHat()
sense.clear()

#get environmental readings
pressure = sense.get_pressure()
humidity = sense.get_humidity()
temperature = sense.get_temperature()
environmentals = [pressure, humidity, temperature]

print_worthy = ", ".join(map(pretty_sense, environmentals))


todays_date = date.today()
date_filename = str(todays_date) + ".txt"

f = open(date_filename, "a")

t = datetime.now()

timestamp_message = t.strftime("%X")

f.write(timestamp_message)
f.close()




