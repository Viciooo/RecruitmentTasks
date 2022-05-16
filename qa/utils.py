import json
import string

import requests
from requests import Response

auth_URL = 'https://restful-booker.herokuapp.com/auth'
booking_URL = 'https://restful-booker.herokuapp.com/booking'
credentials = {"username": "admin",
               "password": "password123"}


def get_token():
    resp: Response = requests.post(auth_URL, credentials)
    token: string = json.loads(resp.text)["token"]
    return token


def get(URL: string):
    resp: Response = requests.get(URL)
    status_code: string = resp.status_code
    if status_code == 404:
        return status_code, None
    else:
        return status_code, resp.json()


def post(URL):
    headers = {"Content-Type": "application/json"}
    data: string = """
    {
        "firstname" : "James",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : true,
        "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    """
    resp: Response = requests.post(URL, headers=headers, data=data)
    return resp


def put(URL):
    headers = {"Content-Type": "application/json", "Accept": "application/json", "Cookie": "token=" + get_token()}

    data: string = """
    {
        "firstname" : "James_updated",
        "lastname" : "Brown_updated",
        "totalprice" : 111,
        "depositpaid" : true,
        "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    """

    resp: Response = requests.put(URL, headers=headers, data=data)
    return resp


def delete(URL):
    headers = {"Content-Type": "application/json", "Cookie": "token=" + get_token()}

    resp: Response = requests.delete(URL, headers=headers)
    return resp


def patch(URL):
    headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorisation": get_token()}

    data = '''{
        "firstname": "James_pached",
        "lastname": "Brown_pached",
    }'''

    resp: Response = requests.patch(URL, headers=headers, data=data)
    return resp


def ping():
    return requests.get('https://restful-booker.herokuapp.com/ping')
