from apiverve_airquality import AirqualityAPIClient
from os import getenv
from dotenv import load_dotenv



load_dotenv()

def main(city: str):
	api = AirqualityAPIClient(getenv("API_KEY_TWO"))
	query = { "city": city }
	result = api.execute(query)
	print(result)
	return city



# url = "https://api.apiverve.com/v1/airquality"

# querystring = {'city': 'chel'}

# headers = {
# 	"x-api-key": getenv("API_KEY_TWO")
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())
	
