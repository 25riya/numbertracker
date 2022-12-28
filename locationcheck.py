import phonenumbers
import folium

#from testing import Api_key
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
# country location
try:
 Number=input("enter your no. with +__:")
 x= phonenumbers.parse(Number)
 time=timezone.time_zones_for_number(x)
 location =geocoder.description_for_number(x,"en")

 print(location)
 print(time)
 #operator name
 operator_name =phonenumbers.parse(Number)
 data=carrier.name_for_number(operator_name,"en")
 print(data)
 key = input("Enter Your API KEY: ")
 geocoder=OpenCageGeocode(key)
 query =str("gwalior,india")
 result = geocoder.geocode(query)

 #print(result)
 lat =result[0]['geometry']['lat']
 lng =result[0]['geometry']['lng']
 print(lat,lng)
 my_map=folium.Map(location=[lat,lng],zoom_start =9)
 folium.Marker([lat,lng],popup=location).add_to(my_map)
 my_map.save("mytracker.html")
except:
    print("Missing or invalid number\nPlease enter your phone number with country code")

