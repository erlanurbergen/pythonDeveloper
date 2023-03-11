import requests
import json

# "https://randomuser.me/api/"

# response = requests.get("https://randomuser.me/api/")
# data = response.json()
#
# with open("data.json", "r") as file:
#     data = json.load(file)
#
#
# print(data["results"][0]["gender"])

response = requests.get("http://apilayer.net/api/live?access_key=0bf99be7ef0f58cfacd22767c59f9458&currencies=&source=USD&format=1")
response_json = response.json()
print(response_json["quotes"]["USDKZT"])
