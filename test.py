import gisapi

client = gisapi.GISAPIClient()

search_results = client.search_data("Florida")
print(search_results)

category_results = client.get_data_by_category("Education and Research")
print(search_results)
