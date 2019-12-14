from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

pressure = sense.get_pressure()
print("Atmospheric pressure is", round(pressure))

humidity = sense.get_humidity()

print("Relative humidity is", round(humidity))
temp = sense.get_temperature()

print("Temperature in Celcius is", round(temp))



