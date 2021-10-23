from thefuzz import fuzz
import json

"""
Install Libraries:
pip install python-Levenshtein
pip install thefuzz
"""


def SearchRestaurant(input):

    with open("data.json") as json_file:

        data = json.load(json_file)
        menu_list = []
        restaurants = data["restaurants"]
        for restaurant in restaurants:
            menu_list.append(restaurant["description"])

    print(menu_list)
    result = []
    for i in range(len(menu_list)):
        if fuzz.token_set_ratio(menu_list[i], input) == 100:
            dict = {
                "siteName": restaurants[i]["siteName"],
                "description": restaurants[i]["description"],
                "address": restaurants[i]["address"],
            }
            result.append(dict)

    if len(result) > 0:
        return result
    else:
        return "Your search - {} - did not match any restaurants.\nSuggestions:\nMake sure all words are spelled correctly.\nTry different keywords.\nTry more general keywords.".format(
            input
        )


input = "sushi"
print(SearchRestaurant(input))
