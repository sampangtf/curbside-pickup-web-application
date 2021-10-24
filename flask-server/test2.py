from hmacHelper import request
import json

# url = "https://api.ncr.com/site/v1/extensions"

# payload = json.dumps({
#     "typeId": {
#         "typeName": "RatingsSet"
#     },
#     "description":
#     "This set is used to show the rating of a restaurant and the number of ratings of a restaurant.",
#     "fields": [{
#         "description": "Indicates the rating of a restaurant.",
#         "fieldName": "Ratings",
#         "fieldType": "NUMBER"
#     }, {
#         "description": "Specifies the number of ratings.",
#         "fieldName": "NumOfRatings",
#         "fieldType": "INTEGER"
#     }]
# })
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization':
#     'AccessKey db9faee31a724296826266906bfb0bc0:j1LmFOQQzX3sxUbCdw272d1sGMf3+4LBYHO+U2cou6dHfEkNrfAylcFEnCg/Jw6HoEjI4zHdqmWJp49spnYQuA==',
#     'nep-organization': 'test-drive-bd96fed4291a4502ac19a',
#     'Date': 'Sat, 23 Oct 2021 20:26:44 GMT'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)


def CreateCustomAttributeSet():
    url = "https://api.ncr.com/site/v1/extensions"
    with open("data.json") as json_file:
        data = json.load(json_file)
        payload = data['custom attribute']
        print(payload)
        response = request(url, "POST", payload)
    return response


CreateCustomAttributeSet()
