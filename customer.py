import json
from hmacHelper import request


def CreateCustomer():
    payload = json.dumps({
        "profileUsername":
        "jshi351@gatech.edu",
        "salutation":
        "Ms",
        "firstName":
        "Kira",
        "middleName":
        "a",
        "lastName":
        "Zheng",
        "effectiveDate":
        "2018-01-20",
        "birthDate":
        "1997-07-22",
        "gender":
        "Female",
        "phone":
        "3748394433",
        "mobile":
        "4857723900",
        "fax":
        "2280001234",
        "identity":
        "identity",
        "homeStore":
        "0123456789",
        "socialSecurityNumber":
        "1245",
        "addresses": [{
            "name": "Home",
            "line1": "699 Spring St NW",
            "line2": "HERE Atlanta 804",
            "city": "Atlanta",
            "state": "GA",
            "postalCode": "30308",
            "extPostalCode": "0000",
            "country": "USA"
        }],
        "identifiersData": [{
            "fieldName": "loyaltyCard",
            "fieldValue": "1234567891",
            "status": "ACTIVE"
        }]
    })
    requestURL = "https://api.ncr.com/cdm/consumers"
    httpMethod = 'POST'
    res = request(requestURL, httpMethod, payload)
    return res


# ConsumerAccountNumber:2JPOAAUBWC1FMQTP
def GetCustomer():
    requestURL = "https://api.ncr.com/cdm/consumers/2JPOAAUBWC1FMQTP"
    httpMethod = "GET"
    payload = {}
    res = request(requestURL, httpMethod, payload)
    return res['data']
