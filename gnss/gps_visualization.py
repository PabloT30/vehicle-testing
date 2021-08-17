from gps_class import GPSVis

# top: 3.3803 - latitude N
# left: -76.5377 - longitude E
# right: -76.5291 - longitude E
# bottom: 3.3675 - latitude N

vis = GPSVis(data_path='moto_test_03-08-2021.csv',
             map_path='map (1).png',  # Path to map downloaded from the OSM.
             points=(3.3803, -76.5377, 3.3675, -76.5291))  # Two coordinates of the map (upper left, lower right)

vis.create_image(color=(0, 0, 255), width=3)  # Set the color and the width of the GNSS tracks.
vis.plot_map(output='save')

print()
