import smbus
import time
bus = smbus.SMBus(1)
address = 0x48

class readAIN:
    def read_AIN0():
        bus.write_byte(address,0x40)
        bus.read_byte(address)
        humi=bus.read_byte(address)
        return(humi)

    def read_AIN1():
        bus.write_byte(address,0x41)
        bus.read_byte(address)
        humi=bus.read_byte(address)
        return(humi)
