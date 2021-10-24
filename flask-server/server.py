from flask import Flask, request
import requests
from flask_cors import CORS
from Restaurant import postRestaurants, getRestaurants
from Customer import createCustomer
from fuzzsearch import SearchRestaurant

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

        # createCustomer(profileUsername, mobile, line1, line2, city, state, postalCode)


@app.route("/search-results", methods=["GET"])
def searchResults():
    k1 = request.args.get("k1")
    k2 = request.args.get("k2")
    results_list_1 = SearchRestaurant(k1)
    results_list_2 = SearchRestaurant(k2)

    if type(results_list_1) == str or type(results_list_2) == str:
        return {"results": results_list_1}

    combinations = []
    for r1 in results_list_1:
        if type(results_list_2) == str:
            combinations.append([r1])
        else:
            for r2 in results_list_2:
                combinations.append([r1, r2])

    return {"results": combinations}


if __name__ == "__main__":
    # Post dummy values to BSP APIs
    # postRestaurants()

    app.run(debug=True)
