import board
import busio
from time import sleep

#from roboticsmasters_bluetoothuart import BluetoothUART


uart = busio.UART(board.GPS_TX, board.GPS_RX, baudrate=9600)

at = b'AT'

uart.write(at)


while True:
    data = uart.readline()

    if data is not None:
        print("data: ", data)
