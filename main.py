# -*- coding: utf-8 -*-
from sel import *
from business import *
import json
from collections import OrderedDict

business_name = "Sturehof"
business_address = "Sturegallerian, Stureplan 2, 114 35 Stockholm, Sweden"

business_id = getBusinessID(business_name, business_address)
print business_id
business_url = getBusinessURL(business_id)
print business_url
getPageSrc(business_url)
contains = containsBusinessView()

response = OrderedDict()
response["name"] = business_name
response["address"] = business_address
response["maps_url"] = business_url
response["hasBusinessView"] = contains

json_response = json.dumps(response)

print json_response