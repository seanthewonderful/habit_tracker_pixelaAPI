import requests
from datetime import datetime


USERNAME = 'seaniwan'
TOKEN = 'hoi23h3029jlk23f90'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# r = requests.post(url=pixela_endpoint, json=user_params)
# print(r.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_params = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_r = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_r.text)

today = datetime.now()
px_today = today.strftime("%Y%m%d")
yesterday = datetime(year=2022, month=6, day=21)
px_yesterday = yesterday.strftime("%Y%m%d")
# print(px_yesterday)

px_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
px_params = {
    "date": px_today,
    "quantity": input("How many minutes did you read yesterday? "),
}

# px_r = requests.post(url=px_endpoint, json=px_params, headers=headers)
# print(px_r.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{px_yesterday}"
update_params = {
    "quantity": "15"
}

# update_r = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(update_r)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{px_today}"

delete_r = requests.delete(url=delete_endpoint, headers=headers)
print(delete_r.text)