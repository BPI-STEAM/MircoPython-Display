from microbit import *

love = Image("01010:"
             "10101:"
             "01010:"
             "00100:"
             "00000")
# 如果你能保证每一行不出错，也可以这样写
# love = Image("01010:10101:01010:00100:00000")

display.show(love)