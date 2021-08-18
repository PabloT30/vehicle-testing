import serial

# ELM327 MINI OBD2 reader with Bluetooth interface.

# Find an open source DBC file https://github.com/commaai/opendbc to convert CAN messages.
# https://www.youtube.com/watch?v=NvYXtQmOYDw
# Datasheet: https://www.elmelectronics.com/wp-content/uploads/2016/07/ELM327DS.pdf

# baudarate can be either 9600 or 38400, see page 8 in datasheet.
# try it using minicom on linux.

with serial.Serial("/dev/ttyUSB0", baudrate=4800) as ser:
    line = str(ser.readline())  # read a '\n' terminated line.
    print(line)
