import time
import board
import busio  # package needs to be installed in venv -> circuitpython?
import adafruit_adxl34x  # package needs to be installed in venv -> circuitpython ding

if __name__=='__main__':
    i2c = busio.I2C(board.SCL, board.SDA)
    accelerometer = adafruit_adxl34x.ADXL345(i2c)

    while True:
        print("%f %f %f" % accelerometer.accelerometer)
        time.sleep(1)
