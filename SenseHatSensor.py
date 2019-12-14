from sense_hat import SenseHat
from datetime import date

sense = SenseHat()

sense.clear()

pressure = sense.get_pressure()
print(pressure)

humidity = sense.get_humidity()

print(humidity)

temp = sense.get_temperature()

print(temp)

ptemp = sense.get_temperature_from_pressure()

print(ptemp)

# ok to start let's get the current date, and then write to a date file
# with recordings every ten minutes. then the next day we start with a new file :)

# fh = open('/home/pi/hack/2019-12-14.txt', 'a+')
# fh.write('Hello Claire')
# fh.close

f = open("2019-12-14.txt", "a")
f.write("Current humidity is:")
f.write(str(humidity))
f.close()