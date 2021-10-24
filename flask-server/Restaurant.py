from hmacHelper import request
import json


def postRestaurants():
    url = "https://gateway-staging.ncrcloud.com/site/sites"

    restaurants = []
    with open("data.json") as json_file:
        data = json.load(json_file)
        for restaurant in data["restaurants"]:
            payload = json.dumps(restaurant)
            response = request(url, "POST", payload)
            restaurants.append(response["data"])
    return restaurants


def getRestaurants():
    restaurants = []
    ref_ids = ["site-001", "site-002"]
    url = "https://gateway-staging.ncrcloud.com/site/sites/by-reference-id/"
    for ref_id in ref_ids:
        restaurant = request(url + ref_id, "GET", {})
        restaurants.append(restaurant)
        print(restaurant)
    return restaurants


# print(getRestaurants())
postRestaurants()
