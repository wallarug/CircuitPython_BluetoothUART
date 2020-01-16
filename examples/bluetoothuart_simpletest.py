import board
import busio

from digitalio import DigitalInOut, Direction, Pull
from time import sleep

#from roboticsmasters_bluetoothuart import BluetoothUART


uart = busio.UART(board.GPS_TX, board.GPS_RX, baudrate=9600)

enable = DigitalInOut(board.SDA)
enable.direction = Direction.OUTPUT

enable.value = True

#state = DigitalInOut(board.SCL)
#state.direction = Direction.INPUT
#print(state.value)

at = b'AT+HELP\r\n'
rt = b'\r\n'

#uart.write(at)


while True:
    
    uart.write(at)
    data = uart.readline()
    #uart.write(at)

    if data is not None:
        print("data: ", data)

    sleep(1)

#bt = BluetoothUART(uart)

#print(bt.connected)
