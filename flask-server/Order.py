import json
from hmacHelper import request
from Customer import GetCustomer

customer = GetCustomer()
print(customer)
# customerID = customer["consumerAccountNumber"]
orderID = "11920734258000737729"


def placeOrder(customer):
    url = "https://gateway-staging.ncrcloud.com/order/3/orders/1"
    payload = json.dumps({"customer": customer, "status": "OrderPlaced"})
    response = request(url, "POST", payload)
    # print(response["data"])


def getOrderByID(orderID):
    url = "https://gateway-staging.ncrcloud.com/order/3/orders/1/" + orderID
    response = request(url, "GET", {})
    return response["data"]


def getOrderByCustomerID(customerID):
    url = "https://gateway-staging.ncrcloud.com/order/3/orders/1/find"
    payload = json.dumps({"consumerID": customerID})
    response = request(url, "POST", payload)


# order = getOrderByID(orderID)
# print(order)
# getOrderByCustomerID(customerID)
