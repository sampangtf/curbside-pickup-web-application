import requests
import urllib3
from urllib.parse import quote

api_key = "AIzaSyBaFmPjFOZznxmoi9f7pEmyCYit2Si8YGk"

def distance_matrix(origin, destination_list, depature_time = "now"):
    origin = quote(origin)
    if len(destination_list) == 1:
        destination = quote(destination_list[0])
    else:
        destination = quote(str("|".join(destination_list)))

    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&departure_time={depature_time}&key={api_key}"

    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    # distance_matrix = response.json()
    return response.json()

def best_routes(origin, destination_list, distance_matrix):
    min_time = 1e99
    min_idx = -1
    npossible_routes = 2
    for idx in range(npossible_routes):
        traveltime = distance_matrix['rows'][0]['elements'][idx]['duration']['value']
        if traveltime < min_time:
            min_time = traveltime
            min_idx = idx

    #####################
    routes = []

    first_destination_address = distance_matrix['destination_addresses'][min_idx]
    first_destination_name = destination_list[min_idx]
    second_idx = [idx for idx in range(npossible_routes) if idx != min_idx][0]
    second_destination_address = distance_matrix['destination_addresses'][second_idx]
    second_destination_name = destination_list[second_idx]

    routes.append((origin, first_destination_name))
    routes.append((first_destination_name, second_destination_name))

    return routes

def finding_directions(routes):
    directions_response = []
    for (origin, destination) in routes:
        url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        directions_response.append(response)
    return [element.json() for element in directions_response]

