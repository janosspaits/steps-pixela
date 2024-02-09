import requests
import json


def read_from_file(filepath):
    with open(filepath, "r") as f:
        return f.readline()


apikey = read_from_file("apikey.txt")
print(apikey)


USERNAME = "janispaits"
pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": apikey,
    "username": "janispaits",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph2",
    "name": "Steps Graph",
    "unit": "steps",
    "type": "int",
    "color": "shibafu",
}

headers = {"X-USER-TOKEN": apikey}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
