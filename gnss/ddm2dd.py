# Coordinates converter from Degree Decimal Minutes DDM to Decimal Degrees DD.

import pandas as pd

# Degrees Minutes.m to Decimal Degrees
# .d = M.m / 60
# Decimal Degrees = Degrees + .d


def latitude_ddm2dd(latitude):
    return round(3 + (round(latitude % 300, 4) / 60), 5)


def longitude_ddm2dd(longitude):
    return -1 * round(76 + (round(longitude % 7600, 4) / 60), 5)


def main():
    data_path = 'Location_Test_GPS_GPRMC_(2021-Aug-03__15_16_44).csv'
    data_ddm = pd.read_csv(data_path, sep=',')

    # data_ddm['latitude_dd'] = data_ddm['latitude'].apply(lambda row: latitude_ddm2dd(row["latitude"]))
    # data_ddm['longitude_dd'] = data_ddm['longitude'].apply(lambda row: longitude_ddm2dd(row["longitude"]))
    data_ddm['latitude_dd_N'] = data_ddm['latitude'].apply(latitude_ddm2dd)
    data_ddm['longitude_dd_E'] = data_ddm['longitude'].apply(longitude_ddm2dd)
    # print(latitude_ddm2dd(data_dd["latitude"][0]))
    # print(longitude_ddm2dd(data_dd["longitude"][0]))
    print(data_ddm[:][["latitude_dd_N", "longitude_dd_E"]].tail(15))
    data_ddm.to_csv("moto_test_03-08-2021.csv", index=False)


if __name__ == "__main__":
    main()
