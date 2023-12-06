# gisapi-sdk-python
Python SDK for GISAPI.io

# Install 
```console
pip install gisapi-sdk
```

## Usage
```python
from gisapi import client

api = client.GISAPIClient()

# regular search query. returns 200 raw results data
search_results = api.search_data("Florida")

# category search. returns 200 raw results from given category
category_results = api.get_data_by_category("Education and Research")

# returns dictionary of layer results in a list
layer_details = api.parse_layer_details(search_results)

# returns just a list of layer urls
layer_urls = api.get_layer_urls(search_results)

# returns list of host urls with no duplicates
host_urls = api.get_host_urls(search_results)
```
