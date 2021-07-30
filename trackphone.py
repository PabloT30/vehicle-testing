import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3

number = "+573216911237"

ch_number = phonenumbers.parse(number, "CH")
print(phonenumbers.geocoder.description_for_number(ch_number, "en"))

service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))

# https://www.google.com/maps/@3.3752536,-76.5324933,18.42z
geolocator = Nominatim(user_agent="trackphone")
location = geolocator.reverse("3.3752536,-76.5324933")
print(location.address)
print(location.latitude, location.longitude)
print(location.raw)

# coordinates = "3.3752536,-76.5324933"
# geolocator = GoogleV3()
# address = geolocator.reverse(coordinates)
# print(address[0])
