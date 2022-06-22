import requests

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

px_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
px_params = {
    "date": "20220621",
    "quantity": "5",
}

px_r = requests.post(url=px_endpoint, json=px_params, headers=headers)
print(px_r.text)