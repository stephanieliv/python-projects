import requests
from datetime import datetime as dt

today = dt.now()

USERNAME = "stephanieliv"
TOKEN = "idnfonofofsfs"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "my coding graph",
    "unit": "hours",
    "type": "int",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours coding?: "),
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "5"
}

# response = requests.put(url=update_pixel, json=new_pixel_data, headers=headers)
# print(response.text)

delete_pixel = f"{pixela_endpoint}/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

delete_pixel_config = {
    "quantity": "0"
}
response = requests.delete(url=delete_pixel, headers=headers)
print(response.text)
