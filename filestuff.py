# ok to start let's get the current date, and then write to a date file
# with recordings every ten minutes. then the next day we start with a new file :)

f = open("2019-12-14.txt", "a")
f.write("Current humidity is:")
f.write(str(humidity))
f.close()

# write a file if it doesn't already exist