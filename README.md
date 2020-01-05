"We journeyed through the night, past the sleeping houses of our countryment."

## About
This is a project aimed at understanding environmental conditions throughout the course of the night.

It uses a Rasberry Pi 4 and Sense Hat to record atmospheric pressure, humidity, and temperature. 


## Structure
ligature.py, pulls readings from hat, prettifies, and writes to file by date

-- utils/
   - blinkatest.py, ensures that the underlying rasberry pi libraries
     		    are sufficient to use the sensehat
   - SenseHatSensory.py, prints out environmental readings from hat. Run this script if you want to get a quick look at the current readings.

## Cron
This script is meant to be used with the Rasberry Pi's local crontab. An example of running the script every night at midnight, 3AM, and 6AM can be found in the file current_crontab in the project's home directory.

In order to use this on your local machine, you'll have to:
1. edit your own crontab. this can be done by running `crontab -e`
2. edit the path in your local cron file to point to the right directory
3. *optional* running the script save_crontab, will just spit out the contents of your current crontab into the local file `current_crontab`.
   
## Hardware List
   (TODO)

## Turning off the RED LED light on Rasberry Pi 4
    ./turn_off_light


