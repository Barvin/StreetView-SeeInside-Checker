import urllib2
import json
import requests
import api_keys

API_KEY = api_keys.google_maps


def getBusinessID(business_name, business_address):
    query = business_name + ", " + business_address
    query = query.replace(" ", "+")
    request_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+query+"&key="+API_KEY

    r = urllib2.urlopen(request_url).read()
    data = json.loads(r)

    for i in data["results"]:
        business_id = i["place_id"]

    return business_id

def getBusinessURL(business_id):
    url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=" + business_id + "&key=" + API_KEY
    r = urllib2.urlopen(url).read()
    data = json.loads(r)

    business_url = data["result"]["url"]
    return business_url


if __name__ == "__main__":
    getBusinessID(business_name, business_address)
    getBusinessURL(business_id)