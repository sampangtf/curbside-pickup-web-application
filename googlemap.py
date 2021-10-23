import requests
import urllib3
from urllib.parse import quote

api_key = "AIzaSyBJ88fUHeMJXZ6DQud9R-PKqFLDFKt-jC0"

def best_routes(origin, destination1, destination2, depature_time = "now"):
    origin = quote(origins)
    destination = quote(f'{destination1}|{destination2}')

    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&departure_time={depature_time}&key={api_key}"

    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    ###########################
    min_time = 1e99
    min_idx = -1
    npossible_routes = 2
    for idx in range(npossible_routes):
        traveltime = response.json()['rows'][0]['elements'][idx]['duration']['value']
        if traveltime < min_time:
            min_time = traveltime
            min_idx = idx

    #####################
    routes = []
    first_destination_address = response.json()['destination_addresses'][min_idx]
    first_destination_name = destinations[min_idx]
    second_idx = [idx for idx in range(npossible_routes) if idx != min_idx][0]
    second_destination_address = response.json()['destination_addresses'][second_idx]
    second_destination_name = destinations[second_idx]

    routes.append((origins, first_destination_name))
    routes.append((first_destination_name, second_destination_name))

    return routes, response.json()

def finding_directions(routes):
    directions_response = []
    for (origin, destination) in routes:
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        directions_response.append(response)
    return [element.json() for element in directions_response]