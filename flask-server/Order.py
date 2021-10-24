import json
from hmacHelper import request
from Customer import GetCustomer

customer = GetCustomer()
print(customer)
# customerID = customer["consumerAccountNumber"]
orderID = "11920734258000737729"


def placeOrder():
    url = "https://gateway-staging.ncrcloud.com/order/3/orders/1"
    payload = json.dumps({"status": "OrderPlaced"})
    response = request(url, "POST", payload)
    return response["data"]


def getOrderByID(orderID):
    url = "https://gateway-staging.ncrcloud.com/order/3/orders/1/" + orderID
    response = request(url, "GET", {})
    return response["data"]


def getOrderByCustomerID(customerID):
    url = "https://gateway-staging.ncrcloud.com/order/3/orders/1/find"
    payload = json.dumps({"consumerID": customerID})
    response = request(url, "POST", payload)
    return response["data"]


# order = getOrderByID(orderID)
# print(order)
# getOrderByCustomerID(customerID)
placeOrder()
