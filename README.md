"We journeyed through the night, past the sleeping houses of our countryment."

## About
This is a project aimed at understanding environmental conditions throughout the course of the night.

It uses a Rasberry Pi 4 and Sense Hat to record atmospheric pressure, humidity, and temperature. 


## Structure
ligature.py, pulls readings from hat, prettifies, and writes to file by date

-- utils/
   - blinkatest.py, ensures that the underlying rasberry pi libraries
     		    are sufficient to use the sensehat
   - SenseHatSensory.py, prints out environmental readings from hat

## Cron
   (TODO)
   
## Hardware List
   (TODO)