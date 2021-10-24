from urllib.parse import urlparse
import base64
import hmac
import hashlib
import requests
from datetime import datetime, timezone

sharedKey = "ba536c561f8f456f8c579ab21e94a99e"
secretKey = "cb1723d601c644668d8786d6ff78bdb1"
nepOrganization = "test-drive-1e47895b4b784893ad73d"


def hmacHelper(
    sharedKey,
    secretKey,
    dateHeader,
    httpMethod,
    requestURL,
    contentType,
    contentMD5,
    nepApplicationKey,
    nepCorrelationID,
    nepOrganization,
    nepServiceVersion,
):
    """
    :param str sharedKey: A user's Shared Key
    :param str secretKey: A user's Secret Key
    :param date date: An unformated date object
    :param str httpMethod: GET/POST/PUT
    :param str requestURL: The API url requesting against
    :param str [contentType=application/json]: Optional
    :param str [nepApplicationKey]: Optional
    :param str [nepCorrelationID]: Optional
    :param str [nepOrganization]: Optional
    :param str [nepServiceVersion]: Optional
    :return: sharedKey:hmac
    :rtype: string
    """
    parsedUrl = urlparse(requestURL)
    pathAndQuery = parsedUrl.path
    if parsedUrl.query:
        pathAndQuery += "?" + parsedUrl.query
    toSign = httpMethod + "\n" + pathAndQuery
    if contentType is not None:
        toSign += "\n" + contentType

    if contentMD5 is not None:
        toSign += "\n" + contentMD5

    if nepOrganization is not None:
        toSign += "\n" + nepOrganization

    if nepApplicationKey is not None:
        toSign += "\n" + nepApplicationKey

    if nepCorrelationID is not None:
        toSign += "\n" + nepCorrelationID

    if nepServiceVersion is not None:
        toSign += "\n" + nepServiceVersion

    isoDate = dateHeader.isoformat(timespec="milliseconds") + "Z"
    key = bytes(secretKey + isoDate, "utf-8")

    message = bytes(toSign, "utf-8")

    digest = hmac.new(key, msg=bytes(message), digestmod=hashlib.sha512).digest()

    signature = base64.b64encode(digest).decode("ascii")

    return sharedKey + ":" + signature


def request(requestURL, httpMethod, payload):
    now = datetime.now(tz=timezone.utc)
    now = datetime(
        now.year,
        now.month,
        now.day,
        hour=now.hour,
        minute=now.minute,
        second=now.second,
    )

    contentType = "application/json"

    hmacAccessKey = hmacHelper(
        sharedKey,
        secretKey,
        now,
        httpMethod,
        requestURL,
        contentType,
        None,
        None,
        None,
        nepOrganization,
        None,
    )

    utcDate = now.strftime("%a, %d %b %Y %H:%M:%S GMT")
    headers = {
        "Date": utcDate,
        "Content-Type": contentType,
        "Authorization": "AccessKey " + hmacAccessKey,
        "nep-organization": nepOrganization,
    }

    if httpMethod == "GET":
        request = requests.get(requestURL, headers=headers)
    elif httpMethod == "POST":
        request = requests.request("POST", requestURL, headers=headers, data=payload)

    res = dict()
    res["status"] = request.status_code
    res["data"] = request.json()

    print(res)

    return res
