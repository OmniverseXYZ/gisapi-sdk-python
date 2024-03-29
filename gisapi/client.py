import requests
import json

class GISAPIClient:
    def __init__(self):
        self.base_url = "https://gisapi.io/api/data"

    def _make_request(self, url):
        """
        Internal method to make HTTP GET requests.
        :param url: The full URL to make the request to.
        :return: JSON response data.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error occurred: {e}")
        except requests.exceptions.Timeout as e:
            print(f"Request timed out: {e}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")

    def search_data(self, query):
        """
        Searches for data based on the given query.
        :param query: The search query.
        :return: A list of search results.
        """
        req_url = f"{self.base_url}/search/{query}"
        return self._make_request(req_url)

    def get_data_by_category(self, category):
        """
        Retrieves data for a specific category.
        :param category: The category to search.
        :return: Data for the specified category.
        """
        req_url = f"{self.base_url}/category/{category}"
        return self._make_request(req_url)
    
    def parse_layer_details(self, response_data):
        """
        Parses layer details from the API response.
        :param response_data: The JSON response data.
        :return: Parsed layer details.
        """
        layer_details = []
        for item in response_data["new_layer_details"]:
            detail = {
                "category": item["CATEGORY"],
                "crs": item["CRS"],
                "url": item["URL"],
                "layer": item["LAYER"],
                "type": item["TYPE"],
                "host": item["HOSTURL"],
                #"extent": json.loads(item["EXTENT"].replace("'", "\""))  # Safely parse the string
            }
            layer_details.append(detail)
        return layer_details

    def parse_xata_details(self, response_data):
        """
        Parses xata details from the API response.
        :param response_data: The JSON response data.
        :return: Parsed xata details.
        """
        xata_details = []
        for item in response_data["new_layer_details"]:
            xata = item.get("xata", {})
            xata_detail = {
                "createdAt": xata.get("createdAt"),
                "updatedAt": xata.get("updatedAt"),
                "score": xata.get("score")
            }
            xata_details.append(xata_detail)
        return xata_details

    def get_layer_urls(self, response_data):
        """
        Extracts and returns all the layer URLs from the API response.
        :param response_data: The JSON response data.
        :return: List of layer URLs.
        """
        urls = []
        for item in response_data.get("new_layer_details", []):
            url = item.get("URL")
            if url:
                urls.append(url)
        return urls
    
    def get_host_urls(self, response_data):
        """
        Extracts and returns all the Host URLs from the API response.
        :param response_data: The JSON response data.
        :return: List of layer URLs.
        """
        urls = []
        for item in response_data.get("new_layer_details", []):
            url = item.get("HOSTURL")
            if url:
                urls.append(url)
        urls = list(set(urls))
        return urls