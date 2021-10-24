import json

import requests
from hmacHelper import request

# response["data"]["consumerAccountNumber"]


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


def GetCustomer():
    requestURL = "https://gateway-staging.ncrcloud.com/cdm/consumers/"
    accountNumber = "XWEKRJFOKNNJRDOA"
    httpMethod = "GET"
    payload = {}
    res = request(requestURL + accountNumber, httpMethod, payload)
    return res["data"]


def createCustomer(profileUsername, mobile, line1, line2, city, state,
                   postalCode):
    url = "https://gateway-staging.ncrcloud.com/cdm/consumers"

    payload = json.dumps({
        "profileUsername":
        profileUsername,
        "mobile":
        mobile,
        "address": [{
            "name": "Home",
            "line1": line1,
            "line2": line2,
            "city": city,
            "state": state,
            "postalCode": postalCode,
        }],
    })

    response = request(url, "POST", payload)
    # print(response["data"])


def CreateCustomAttributeSet():
    url = "https://gateway-staging.ncrcloud.com/site/extensions"
    with open("data.json") as json_file:
        data = json.load(json_file)
        payload = json.dumps(data['custom attribute'])
        print(payload)
    response = request(url, "POST", payload)
    return response


CreateCustomAttributeSet()
