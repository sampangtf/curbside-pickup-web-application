import json
from hmacHelper import request


def CreateCustomer():
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
    accountNumber = "2JPOAAUBWC1FMQTP"
    httpMethod = "GET"
    payload = {}
    res = request(requestURL + accountNumber, httpMethod, payload)
    return res["data"]


def CreateCustomAttributeSet():
    url = "https://gateway-staging.ncrcloud.com/site/v1/extensions"
    with open("data.json") as json_file:
        data = json.load(json_file)
        payload = json.dumps(data['custom attribute'])
        print(payload)
    response = request(url, "POST", payload)
    return response


print(CreateCustomAttributeSet())
