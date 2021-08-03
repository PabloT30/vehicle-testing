import pandas as pd

data_path = 'Location_Test_GPS_GPRMC_(2021-Jul-30__12_44_45).csv'
data_dmm = pd.read_csv(data_path, sep=',')
data_dd = data_dmm[:][["latitude", "longitude"]]

print(data_dd.head())
