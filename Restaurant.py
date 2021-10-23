import http.client
from base64 import b64encode
import requests


class Restaurant:
    def __init__(self, address, contact, enterpriseUnitName, description, name) -> None:

        payload = (
            '{"address":{"city":'
            + address["city"]
            + ',"country":'
            + address["country"]
            + ',"postalCode":'
            + address["postalCode"]
            + ',"state":'
            + address["state"]
            + ',"street":'
            + address["street"]
            + '},"contact":{"contactPerson":'
            + contact["contactPerson"]
            + ',"phoneNumber":'
            + contact["phoneNumber"]
            + ',"phoneNumberCountryCode":'
            + contact["phoneNumberCountryCode"]
            + '},"coordinates":{"latitude":'
            + address["latitude"]
            + ',"longitude":'
            + address["longitude"]
            + '},"description":'
            + description
            + ',"enterpriseUnitName":'
            + enterpriseUnitName
            + ',"siteName":'
            + name
            + "}"
        )

        # userAndPass = b64encode(
        #     b"test-drive-1e47895b4b784893ad73d:92350a4b-45a5-42c6-8c95-ad0c5c2268b8"
        # )

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "nep-organization": "b",
            "nep-correlation-id": "b",
            # "Authorization": "Basic test-drive-1e47895b4b784893ad73d:92350a4b-45a5-42c6-8c95-ad0c5c2268b8",
            # "AccessKey": "56b538fcaba047edba1165b00affcf56",
        }

        # userAndPass = b64encode(b"username:password").decode("ascii")
        # headers = {"Authorization": "Basic %s" % userAndPass}

        # requests.post(
        #     "http://api.ncr.com/site/v1/sites",
        #     headers,
        #     auth=(
        #         "test-drive-1e47895b4b784893ad73d",
        #         "92350a4b-45a5-42c6-8c95-ad0c5c2268b8",
        #     ),
        # )

        url = "https://api.ncr.com/site/v1/sites"

        obj = {
            "coordinates": {
                "latitude": address["latitude"],
                "longitude": address["longitude"],
            },
            "enterpriseUnitName": enterpriseUnitName,
            "siteName": name,
        }

        response = requests.post(
            url, data=obj, headers=headers, auth=(username, password)
        )

        print(response.text)

        # conn.request("POST", "/site/v1/sites", payload, headers)

        # res = conn.getresponse()
        # data = res.read()

        # print(data.decode("utf-8"))

    def get_address(self):
        pass


api_key = ""

if __name__ == "__main__":
    conn = http.client.HTTPSConnection("api.ncr.com")
    username = "test-drive-1e47895b4b784893ad73d"
    password = "92350a4b-45a5-42c6-8c95-ad0c5c2268b8"

    # Restaurant 1
    address = {
        "city": '"Atlanta"',
        "country": '"USA"',
        "postalCode": '"30308"',
        "state": '"GA"',
        "street": '"860 Spring St. NW"',
        "latitude": "33.6817952",
        "longitude": "-84.4239568",
    }
    contact = {
        "contactPerson": '"Jane Austen"',
        "phoneNumber": '"1112223333"',
        "phoneNumberCountryCode": '"1"',
    }
    description = (
        '"A customer-favorite sushi restaurant with in the heart of Atlanta Midtown."'
    )
    enterpriseUnitName = '"Jane\'s Kitchen"'
    name = '"Jane\'s Kitchen"'

    r1 = Restaurant(address, contact, enterpriseUnitName, description, name)

    # conn = http.client.HTTPSConnection("api.ncr.com")

    # payload = '{"address":{"city":"Atlanta","country":"USA","postalCode":"30308","state":"GA","street":"860 Spring St. NW"},"contact":{"contactPerson":"George Burdell","phoneNumber":"6787323274","phoneNumberCountryCode":"44"},"coordinates":{"latitude":33.6817952,"longitude":-84.4239568},"currency":"USD","customAttributeSets":[{"attributes":[{"key":"String","value":"String"}],"typeName":"String"}],"dayparts":[],"description":"A state-of-the-art campus designed to attract top talent, showcase NCRs technology solutions and serve as an iconic landmark for the City of Atlanta.","enterpriseUnitName":"NCR World Headquarters","hours":[],"id":"a6c0b9c5ed4c40f8bf584dca562b47eb","locked":true,"parentEnterpriseUnitId":"a6c0b9c5ed4c40f8bf584dcb562b47eb","referenceId":"String","siteName":"NCR\'s World Headquarters","status":"ACTIVE","timeZone":"US/Eastern"}'

    # headers = {
    #     "accept": "application/json",
    #     "content-type": "application/json",
    #     "nep-organization": "SOME_STRING_VALUE",
    #     "Accept": "application/json",
    #     "nep-correlation-id": "SOME_STRING_VALUE",
    #     "Content-Type": "application/json",
    # }

    # conn.request("POST", "/site/v1/sites", payload, headers)

    # res = conn.getresponse()
    # data = res.read()

    # print(data.decode("utf-8"))
