#! /usr/bin/python3

# mishmosh of the other files
# this may end up being the useful one
from datetime import datetime
from datetime import date
from sense_hat import SenseHat

# helper fns
def pretty_sense(sensory):
    return (str(round(sensory)))

def make_timestamp(t):
    return t.strftime("%X") + ": "

def build_file_row(t, environmentals):
    return make_timestamp(t) + environmentals + "\n"

def convert_fahrenheit(celcius):
    return (celcius * 9/5) + 32

# initialize sensor
sense = SenseHat()
sense.clear()

# get environmental readings
pressure = sense.get_pressure()
humidity = sense.get_humidity()
temperature = sense.get_temperature()

# format environmental readings
sensors = [pressure, humidity, convert_fahrenheit(temperature)]
print_worthy_sensors = ", ".join(map(pretty_sense, sensors))

# flesh out some useful date info
todays_date = date.today()
date_filename = str(todays_date) + ".txt"
t = datetime.now()

# combine date and sense data into the message
# we'll actually append to the file
timestamp_message = build_file_row(t, print_worthy_sensors)

# open today's file & write timestamped environmental data to it
f = open(date_filename, "a")
f.write(timestamp_message)
f.close()




