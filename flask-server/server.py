from flask import Flask, request
import requests
from flask_cors import CORS
from Restaurant import postRestaurants, getRestaurants
from Customer import createCustomer
from fuzzsearch import SearchRestaurant
from Order import placeOrder, getOrderByID, getOrderByCustomerID
from Ranking import combination_ranking


# from Ranking import restaurant_rank
import json

app = Flask(__name__)
CORS(app)

restaurants = getRestaurants()


@app.route("/restaurants", methods=["GET"])
def getRestaurants():
    try:
        return {"restaurants": restaurants}
    except:
        pass


@app.route("/customers", methods=["GET", "POST"])
def customers():
    if request.method == "POST":
        profileUsername = request.args.get("profileUsername")
        mobile = request.args.get("mobile")
        line1 = request.args.get("line1")
        line2 = request.args.get("line2")
        city = request.args.get("city")
        state = request.args.get("state")
        postalCode = request.args.get("postalCode")

        customer = createCustomer(
            profileUsername, mobile, line1, line2, city, state, postalCode
        )
        return {"results": customer}
    else:
        return {"foo": "bar"}


@app.route("/search-results", methods=["GET"])
def searchResults():
    k1 = request.args.get("k1")
    k2 = request.args.get("k2")
    results_list_1 = SearchRestaurant(k1)
    results_list_2 = SearchRestaurant(k2)

    if type(results_list_1) == str or type(results_list_2) == str:
        return {
            "results": "false",
        }

    combinations = []
    for r1 in results_list_1:
        if type(results_list_2) == str:
            combinations.append([r1])
        else:
            for r2 in results_list_2:
                combinations.append([r1, r2])

    with open("data.json") as json_file:
        data = json.load(json_file)
        origin = data["customer_cite"][0]["siteName"]
    (
        sorted_combinations,
        total_traveltime_list,
        weighted_rating_list,
    ) = combination_ranking(combinations, origin)
    return {
        "results": {
            "combinations": sorted_combinations,
            "distance_list": total_traveltime_list,
            "avg_rating_list": weighted_rating_list,
        }
    }


@app.route("/orders", methods=["POST", "GET"])
def orders():
    if request.method == "POST":
        return {"results": placeOrder()}
    elif request.method == "GET":
        orderID = request.args.get("id")
        order = getOrderByID(orderID)
        return {
            "id": order["id"],
            "status": order["status"],
            "dateCreated": order["dateCreated"],
        }


if __name__ == "__main__":
    # Post dummy values to BSP APIs
    # postRestaurants()

    app.run(debug=True)
