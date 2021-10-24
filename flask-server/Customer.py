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


def CreateCustomAttributeSet():
    url = "https://api.ncr.com/site/v1/extensions"
    with open("data.json") as json_file:
        data = json.load(json_file)
        payload = data['custom attribute']
        print(payload)
    response = request(url, "POST", payload)
    return response


print(CreateCustomAttributeSet())
