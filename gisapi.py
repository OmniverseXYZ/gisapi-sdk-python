import requests

class GISAPIClient:
    def __init__(self):
        self.base_url = "https://www.gisapi.io/api/data"

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

    def get_data_by_id(self, record_id):
        """
        NOT YET IMPLEMENTED
        Retrieves data for a specific record ID.
        :param record_id: The ID of the record to retrieve.
        :return: Data for the specified record.
        """
        req_url = f"{self.base_url}/data/record/{record_id}"
        return self._make_request(req_url)