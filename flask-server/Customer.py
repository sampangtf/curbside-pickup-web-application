import json

import requests
from hmacHelper import request


def PostCustomers():
    url = "https://gateway-staging.ncrcloud.com/cdm/consumers"

    customers = []
    with open("data.json") as json_file:
        data = json.load(json_file)
        for customer in data["customers"]:
            payload = json.dumps(customer)
            response = request(url, "POST", payload)
            customers.append(response["data"])
    return customers


def createCustomer(profileUsername, mobile, line1, line2, city, state, postalCode):
    url = "https://gateway-staging.ncrcloud.com/cdm/consumers/"

    payload = json.dumps(
        {
            "profileUsername": profileUsername,
            "mobile": mobile,
            "addresses": [
                {
                    "name": "Home",
                    "line1": line1,
                    "line2": line2,
                    "city": city,
                    "state": state,
                    "postalCode": postalCode,
                }
            ],
        }
    )

    response = request(url, "POST", payload)
    return response["data"]


def CreateCustomAttributeSet():
    url = "https://gateway-staging.ncrcloud.com/site/v1/extensions"
    with open("data.json") as json_file:
        data = json.load(json_file)
        payload = data["custom attribute"]
        print(payload)
    response = request(url, "POST", payload)
    return response


<<<<<<< HEAD
PostCustomers()
=======
# print(CreateCustomAttributeSet())
createCustomer("a00", "1112223039", "99 St Ne", "805", "Atlanta", "GA", "30308")


# def GetCustomer():
#     requestURL = "https://api.ncr.com/cdm/consumers/"
#     accountNumber = "2JPOAAUBWC1FMQTP"
#     httpMethod = "GET"
#     payload = {}
#     res = request(requestURL + accountNumber, httpMethod, payload)
#     return res["data"]
# >>>>>>> f4300ad4cedb4c4f7f9ba859e293cf74f9a11d2a
