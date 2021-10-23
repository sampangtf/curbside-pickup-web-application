from thefuzz import fuzz
import json
"""
Install Libraries:
pip install python-Levenshtein
pip install thefuzz
"""


def SearchRestaurant(input):

    with open("Data.json") as json_file:

        data = json.load(json_file)
        menu_list = []
        restaurants = data["restaurants"]
        for restaurant in restaurants:
            menu_list.append(restaurant['description'])
        # for restaurant in data["restaurants"]:
        #     payload = json.dumps(restaurant)
        #     response = request(url, "POST", payload)
        #     restaurants.append(response["data"])

    result = []
    for i in range(len(menu_list)):
        if fuzz.token_set_ratio(menu_list[i], input) == 100:
            dict = {
                'siteName': restaurants[i]['siteName'],
                'description': restaurants[i]['description'],
                'address': restaurants[i]['address']
            }
            result.append(dict)

    if len(result) > 0:
        return json.dumps(result)
    else:
        print("Your search - " + input + """ - did not match any restaurants.\n
Suggestions:\n
Make sure all words are spelled correctly.\n
Try different keywords.\n
Try more general keywords.""")
        return


input = "sushi"
print(SearchRestaurant(input))
