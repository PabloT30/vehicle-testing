import serial
import time
import csv
from datetime import datetime

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

# E.g. $GPRMC,225446,A,4916.45,N,12311.12,W,000.5,054.7,191194,020.3,E*68
#      0       1     2  3      4  5       6   7    8      9     10   11 12

# Position  | Variable          | Example       | Description
# 0         | Sentence          | GPRMC         | GPS sentence
# 1         | Time Stamp        | 225446        | Time of fix 22:54:46 UTC - hhmmss
# 2         | Validity          | A             | Navigation receiver warning A = OK, V = warning-invalid
# 3         | Current latitude  | 4916.45       | dd° mm.mmm' Latitude 49 deg. 16.45 min N/S.
# 4         | North/South       | N             | North/South latitude.
# 5         | Current longitude | 12311.12      | Longitude 123 deg. 11.12 min E/W.
# 6         | East/West         | E             | East/West longitude.
# 7         | Speed in knots    | 000.5         | Speed over ground in Knots -> * 1.852 to convert to kmh
# 8         | True course       | 054.7         | Course Made Good, True
# 9         | Date Stamp        | 191194        | Date of fix  19 November 1994 - ddmmyy
# 10        | Variation         | 020.3,E       | Magnetic variation 20.3 deg
# 11        | East/West         | E             | East/West magnetic variation
# 12        | Checksum          | *68           | Mandatory checksum

# tiempo = 225446
# fecha = 300721
#
#
# def to_timestamp(time_, date_):
#     time_ = str(time_)
#     date_ = str(date_)
#     time_ = f"{time_[0:2]}:{time_[2:4]}:{time_[4:]} UTC"
#     date_ = f"20{date_[4:]}-{date_[0:2]}-{date_[2:4]}"
#     return date_ + ' ' + time_

# ISO 8601 standardizes the representation of dates and times.[2]
# These standard representations are often used to construct timestamp values.


# print(to_timestamp(tiempo, fecha))

# "COM5" para Windows.
# Bus 001 Device 005: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port
# usb 1-1.2: pl2303 converter now attached to ttyUSB0

# What are the different GPS coordinate formats?
# Here are examples of formats that work:
# Degrees, minutes, and seconds (DMS): 41°24'12.2"N 2°10'26.5"E.
# Degrees and decimal minutes (DMM): 41 24.2028, 2 10.4418.
# Decimal degrees (DD): 41.40338, 2.17403.

# to do convert from DMM to DD to plot on map.png
# to do export to GPX file and display track on OpenStreetMap https://www.openstreetmap.org/traces/new

with serial.Serial("/dev/ttyUSB0", baudrate=4800) as ser:
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
                                              str(round(float(data[7]) * 1.852, 2)), data[8], data[9], data[10],
                                              data[11]])
