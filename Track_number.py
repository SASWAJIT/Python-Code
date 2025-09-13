# import phonenumbers
# from phonenumbers import geocoder
# phone_number1= geocoder.parse("+919348599317")
# print(phone_number1)


# a=int(input("enter first range"))
# b=int(input("enter second range"))
# for num in range(a, b+1):
#       for i in range(2,num):
#         if(num%i) == 0:
#             break
#       else :
#             print(num)

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium


key = "your key" #Geocoder API Key need to paste here "your key" 
number = input("please giver your number: ")
new_number = phonenumbers.parse(number)
location = geocoder.description_for_number(new_number, "en")
print(location)

service_name = carrier.name_for_number(new_number,"en")
print(service_name)

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

my_map = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat, lng], popup= location).add_to(my_map)

my_map.save("location.html")

print("location tracking completed")
print("Thank you")
