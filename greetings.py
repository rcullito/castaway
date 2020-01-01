from sense_hat import SenseHat
sense = SenseHat()


#.05 will scroll at twice the usual speed
# bigger the number, slower the speed

# red, green, blue
#sense.show_message("Hello, World!", text_colour=(255, 255, 0),
 #                  back_colour=(0,0,0),
  #                 scroll_speed=(0.05))

# success
sense.show_message("Success", text_colour=(0,255,0))

sense.show_message("Failure", text_colour=(255,0,0))


