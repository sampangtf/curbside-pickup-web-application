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


def CreateCustomAttributeSet():
    url = "https://gateway-staging.ncrcloud.com/site/v1/extensions"
    with open("data.json") as json_file:
        data = json.load(json_file)
        payload = json.dumps(data["custom attribute"])
    response = request(url, "POST", payload)
    return response


def UpdateCustomAttributes():
    ratings = []

    # ref_ids = ["site-001", "site-002", "site-003", "site-004", "site-005", "site-006", "site-007", "site-008","site-009"]
    url = "https://gateway-staging.ncrcloud.com/site/v1/sites/"

    with open("data.json") as json_file:
        data = json.load(json_file)
        restaurants = data["restaurants"]
        ref_ids = [i["referenceId"] for i in restaurants]
        for i in range(len(data["ratings"])):
            payload = json.dumps(data["ratings"][i])
            getid = request(
                "https://gateway-staging.ncrcloud.com/site/sites/by-reference-id/"
                + ref_ids[i], "GET", {})
            response = request(url + getid['data']['id'], "PATCH", payload)
            ratings.append(response["data"])
    return ratings


def GenerateRestaurants():
    CreateCustomAttributeSet()
    postRestaurants()
    RestaurantRatings = UpdateCustomAttributes()
    return RestaurantRatings
