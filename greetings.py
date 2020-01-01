from sense_hat import SenseHat
sense = SenseHat()


#.05 will scroll at twice the usual speed
sense.show_message("Hello, World!", text_colour=(255, 255, 0),
                   back_colour=(0,0,255),
                   scroll_speed=(0.05))