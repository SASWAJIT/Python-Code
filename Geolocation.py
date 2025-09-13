# import requests

# def reverse_geocode(lat, lng, api_key):
#     url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}"
#     response = requests.get(url)
#     return response.json() if response.status_code == 200 else None

# # Example usage:
# latitude = 40.714224
# longitude = -73.961452
# api_key = ""
# location_data = reverse_geocode(latitude, longitude, api_key)
# if location_data:
#     print(location_data)

s= "saswajit pari da"
k=s.replace(" ","")
print(k)