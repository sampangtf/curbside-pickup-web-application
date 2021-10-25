import requests
import urllib3
from urllib.parse import quote
from itertools import permutations
from config import api_key


def distance_matrix(origin, destination_list, depature_time="now"):
    origin = quote(origin)
    if len(destination_list) == 1:
        destination = quote(destination_list[0])
    else:
        destination = quote(str("|".join(destination_list)))

    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&departure_time={depature_time}&key={api_key}"

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    # distance_matrix = response.json()
    return response.json()


def best_routes(origin, destination_list):
    min_time = 1e99
    min_idx = -1
    # npossible_routes = 2

    possible_routes = list(permutations(destination_list))
    total_traveltime_list = []
    for route in possible_routes:
        traveltime = 0
        print(route)
        traveltime = distance_matrix(origin, route[0])["rows"][0]["elements"][0][
            "duration"
        ][
            "value"
        ]  # first leg
        for idx, destination in enumerate(route[0:-1]):
            traveltime += distance_matrix(route[idx], route[idx + 1])["rows"][0][
                "elements"
            ][0]["duration"]["value"]
        total_traveltime_list.append(traveltime)
    sorted_routes = sorted(
        possible_routes, key=lambda x: total_traveltime_list[possible_routes.index(x)]
    )
    sorted_traveltime_list = sorted(total_traveltime_list)

    print(possible_routes, total_traveltime_list)

    best_route = sorted_routes[0]
    travel_time = sorted_traveltime_list[0]

    return best_route, travel_time


def finding_directions(routes):
    directions_response = []
    for (origin, destination) in routes:
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        directions_response.append(response)
    return [element.json() for element in directions_response]
