#from .gisapi import client
#from . import gisapi
import gisapi
from gisapi import client

api = client.GISAPIClient()

try:
    search_results = api.search_data("Florida")
    print(search_results)
except:
    print("search_results FAILED")

try:
    category_results = api.get_data_by_category("Education and Research")
    print(search_results)
except:
    print("category_results FAILED")

try:
    layer_details = api.parse_layer_details(search_results)
    print(layer_details)
except:
    print("layer_details FAILED")

try:
    xata_details = api.parse_xata_details(search_results)
    print(xata_details)
except:
    print("xata_details FAILED")

try:
    layer_urls = api.get_layer_urls(search_results)
    print(layer_urls)
except:
    print("layer_urls FAILED")

try:
    host_urls = api.get_host_urls(search_results)
    print(host_urls)
except:
    print("host_urls FAILED")