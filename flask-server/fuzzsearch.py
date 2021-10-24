from thefuzz import fuzz
from Restaurant import GenerateRestaurants
import json

"""
Install Libraries:
pip install python-Levenshtein
pip install thefuzz
"""


def SearchRestaurant(input):

    menu_list = []
    # restaurants = data["restaurants"]
    restaurants = GenerateRestaurants()
    for restaurant in restaurants:
        menu_list.append(restaurant["description"])

    # print(menu_list)
    result = []
    for i in range(len(menu_list)):
        if fuzz.token_set_ratio(menu_list[i], input) == 100:
            dict = {
                "siteName": restaurants[i]["siteName"],
                "description": restaurants[i]["description"],
                "address": restaurants[i]["address"],
                "customAttributeSets": restaurants[i]["customAttributeSets"],
            }
            result.append(restaurants[i])

    if len(result) > 0:
        return result
    else:
        return ""


input = "sushi"
print(SearchRestaurant(input))
