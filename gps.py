import serial
import time
import csv

# protocol to work with GPS: NMEA
# it has different sentences like GPRMC.
# https://www.youtube.com/watch?v=_DuMjcl52BU
# b'$GPRMC,151910.000,A,0322.0902,N,07631.9756,W,0.46,196.83,300721,,,A*77\r\n'
# Latitude:66 0322.0902
# Longitude: 07631.9756
# http://aprs.gids.nl/nmea/#rmc
# dd° mm.mmm'
# https://www.geoplaner.com/

moment = time.strftime("%Y-%b-%d__%H_%M_%S", time.localtime())
header_flag = True
header = ['time_stamp', 'latitude', 'north/south', 'longitude', 'east/west',
          'speed_kmh', 'true_course', 'date_stamp', 'variation', 'east/west']


with serial.Serial("COM5", baudrate=4800) as ser:
    while True:
        line = str(ser.readline())  # read a '\n' terminated line.
        data = line.split(',')
        if data[0] == "b'$GPRMC":
            if data[2] == 'A':
                print(line)
                with open("Location_Test_GPS_GPRMC_(" + moment + ").csv", 'a', newline='') as loc_test_file:
                    loc_test_writer = csv.writer(loc_test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    if header_flag:
                        header_flag = False
                        loc_test_writer.writerow(header)
                    loc_test_writer.writerow([data[1], data[3], data[4], data[5], data[6],
                                              str(round(float(data[7]) * 1.852, 2)), data[8], data[9], data[10], data[11]])
