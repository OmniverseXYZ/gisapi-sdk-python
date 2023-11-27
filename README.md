# gisapi-sdk-python
Python SDK for GISAPI.io

## Usage
Not currently on PyPi (coming soon).
clone repo into project or download and move gisapi.py file into project. 
```python
import gisapi

client = gisapi.GISAPIClient()

# regular search query. returns 200 results
search_results = client.search_data("Florida")

# returns 200 results from given category
category_results = client.get_data_by_category("Education and Research")
```
