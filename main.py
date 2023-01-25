from machine import Pin, I2C
import ssd1306
from time import sleep
import dht

# ESP32 Pin assignment 
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

sensor = dht.DHT22(Pin(23))
while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print('Suhu: %3.1f C' %temp)
    print('Kelembapan: %3.1f %%' %hum)

    oled.text('Suhu: ' , 0, 10)
    oled.text('  %3.1f C' %temp, 0, 20)
    oled.text('kelembapan:' , 0, 30)
    oled.text('  %3.1f %%'  %hum , 0, 40)

    oled.show()

  except OSError as e:
    print('Failed to read sensor.')