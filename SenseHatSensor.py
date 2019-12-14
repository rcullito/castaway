from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

pressure = sense.get_pressure()
print("Atmospheric pressure is", pressure)

humidity = sense.get_humidity()

print("Relative humidity is", humidity)

temp = sense.get_temperature()

print("Temperature in Celcius is", temp)



# ok to start let's get the current date, and then write to a date file
# with recordings every ten minutes. then the next day we start with a new file :)

f = open("2019-12-14.txt", "a")
f.write("Current humidity is:")
f.write(str(humidity))
f.close()