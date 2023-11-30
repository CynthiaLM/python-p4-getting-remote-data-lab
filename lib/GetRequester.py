import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        response = requests.get(url)
        return response.content

    def load_json(self):
       response_body = self.get_response_body()
       if not response_body:
            print("Error: Empty response body.")
            return None
       try:
            json_data = json.loads(response_body)
       except json.JSONDecodeError:
            print("Error: Unable to decode JSON.")
            return None

       if isinstance(json_data, (list, dict)):
            return json_data
       else:
            print("Error: Unexpected JSON format.")
            return None