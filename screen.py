from machine import Pin, I2C
from picobricks import SSD1306_I2C
i2c = I2C(0, scl=Pin(5), sda=Pin(4))  
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)

'''
Available commands
oled.fill(0) Fill with color
oled.blit(fb2, 0, 0) Show buffer
oled.show() Actualize
oled.pixel(x, y, 0) Show a pixel
oled.scroll(speed,0) ??
oled.text("string", x, y) 
'''








oled.show()