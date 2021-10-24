import json
from hmacHelper import request


def CreateCustomer():
    url = "https://api.ncr.com/cdm/consumers"

    customers = []
    with open("data.json") as json_file:
        data = json.load(json_file)
        for customer in data["customers"]:
            payload = json.dumps(customer)
            response = request(url, "POST", payload)
            customers.append(response["data"])
    return customers


def GetCustomer():
    requestURL = "https://api.ncr.com/cdm/consumers/"
    accountNumber = "2JPOAAUBWC1FMQTP"
    httpMethod = "GET"
    payload = {}
    res = request(requestURL + accountNumber, httpMethod, payload)
    return res["data"]
