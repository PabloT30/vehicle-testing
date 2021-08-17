import time
import serial

moment = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())

with serial.Serial("COM6", baudrate=4800) as ser:
    while True:
        line = str(ser.readline())  # read a '\n' terminated line.
        print(line)
        with open("NMEA_Test_(" + moment + ").csv", 'a', newline='') as nmea_test_file:
            nmea_test_file.write(line + "\n")
