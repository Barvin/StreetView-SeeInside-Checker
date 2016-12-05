# -*- coding: utf-8 -*-
from sel import *
from business import *
import json
from collections import OrderedDict

#Test values
business_name = "Sturehof"
business_address = "Sturegallerian, Stureplan 2, 114 35 Stockholm, Sweden"

business_id = getBusinessID(business_name, business_address)
business_url = getBusinessURL(business_id)
getPageSrc(business_url)
contains = containsBusinessView()

"""
Creates JSON response from Dictionary
"""
response = OrderedDict()
response["name"] = business_name
response["address"] = business_address
response["maps_url"] = business_url
response["hasBusinessView"] = contains

json_response = json.dumps(response)

print json_response