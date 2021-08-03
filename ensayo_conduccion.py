import pandas as pd

data = pd.read_csv("Location_Test_GPS_GPRMC_(2021-Aug-03__15_16_44).csv", delimiter=",")
print(data.head())
print(data.columns)
print(max(data[:]["speed_kmh"]))
