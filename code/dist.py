import googlemaps
from datetime import datetime
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


key = os.environ.get("GOOGLE_MAPS_API_KEY")
gmaps = googlemaps.Client(key=str(key))
now = datetime.now()


def distance(origin, destination):
    directions_result = gmaps.directions(origin, destination, departure_time=now)
    dist = directions_result[0]["legs"][0]["distance"]["text"]
    if dist[::-1][0:2] == "tf":  # ft backwards
        return 1
    return round(float(dist[:-3].replace(",", "")))


print(distance("seattle", "washington dc"))
print(distance("53792", "53792"))
print(
    distance(
        "Venture, 619 N Segoe Rd, Madison, WI 53705",
        "SpringHill Suites by Marriott Madison, 4601 Frey St, Madison, WI 53705",
    )
)
