import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyA6IFdGXrMb2s-rC7eShps0ew5ntbWuUyQ')
now = datetime.now()

def distance(origin, destination):
    directions_result = gmaps.directions(origin, destination, departure_time=now)
    dist = directions_result[0]["legs"][0]["distance"]["text"]
    if dist[::-1][0:2] == "tf": #ft backwards
        return 1
    return round(float(dist[:-3].replace(',',"")))
 

print(distance("seattle", "washington dc"))
print(distance("Venture, 619 N Segoe Rd, Madison, WI 53705", "SpringHill Suites by Marriott Madison, 4601 Frey St, Madison, WI 53705"))