from microbit import *

Red=(2, 0, 0)
love1 = Image("01010:"
             "10101:"
             "01010:"
             "00100:"
             "00000")

love2 = Image("00000:"
             "01010:"
             "10101:"
             "01010:"
             "00100")

love3 = Image("00000:"
             "00000:"
             "01010:"
             "10101:"
             "01010")

love4 = Image("00000:"
             "00000:"
             "00000:"
             "01010:"
             "10101")

love5 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "01010")

love6 = Image("00000:"
              "00000:"
              "00000:"
              "00000:"
              "00000")

all_loves = [love1, love2, love3, love4, love5, love6]
display.show(all_loves, delay=500, loop=True,color=Red)