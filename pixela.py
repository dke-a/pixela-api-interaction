import requests
import hashlib
from datetime import datetime
from utils import get_hashed_token, clear_screen

PIXELA_BASE_URL = "https://pixe.la/v1/users/"

def make_pixela_request(endpoint, method="get", data=None, token=None):
    """Makes a request to the Pixela API."""
    headers = {}
    if token:
        headers["X-USER-TOKEN"] = get_hashed_token(token)

    if method.lower() == "get":
        response = requests.get(url=endpoint, headers=headers)
    elif method.lower() == "post":
        response = requests.post(url=endpoint, json=data, headers=headers)
    elif method.lower() == "put":
        response = requests.put(url=endpoint, json=data, headers=headers)
    elif method.lower() == "delete":
        response = requests.delete(url=endpoint, headers=headers)
    else:
        raise ValueError("Invalid HTTP method")

    return response

def get_user_graphs(username, token):
    """Retrieves a list of all graphs for a user and returns their IDs and names."""
    endpoint = f"{PIXELA_BASE_URL}{username}/graphs"
    response = make_pixela_request(endpoint, token=token)
    json_data = response.json()
    graphs = json_data.get('graphs', [])
    print(endpoint)
    return [(graph['id'], graph['name']) for graph in graphs]

def print_graphs(graphs):
    """Prints the IDs and names of user's graphs."""
    for graph_id, graph_name in graphs:
        print(f"- ID: {graph_id}, Name: {graph_name}")

def create_user():
    """Creates a new Pixela user account."""
    username = input("Enter desired username: ")
    token = input("Enter your Pixela token: ")
    hashed_token = get_hashed_token(token)
    user_params = {
        "token": hashed_token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    endpoint = PIXELA_BASE_URL
    response = make_pixela_request(endpoint, method="post", data=user_params, token=token)
    print(response.text)
    print(endpoint)

def create_graph(username, token, graphs):
    """Creates a new graph on Pixela."""
    graph_id = input("Enter graph ID: ")
    graph_name = input("Enter graph name: ")
    unit = input("Enter unit: ")
    graph_type = input("Enter type (int or float): ")
    color = input("Enter color (Enter color (shibafu/grass, momiji/red, sora/blue, ichou/yellow, ajisai/purple, kuro/black): ")
    
    graph_config = {
        "id": graph_id,
        "name": graph_name,
        "unit": unit,
        "type": graph_type,
        "color": color
    }
    endpoint = f"{PIXELA_BASE_URL}{username}/graphs"
    response = make_pixela_request(endpoint, method="post", data=graph_config, token=token)
    print(response.text) 
    print(endpoint)

def post_pixel(username, token, graphs):
    """Posts a new data point to a Pixela graph."""
    print("Available graphs:")
    print_graphs(graphs)
    graph_id = input("Enter graph ID: ")
    date = input("Enter date (YYYYMMDD): ")
    quantity = input("Enter quantity: ")
    endpoint = f"{PIXELA_BASE_URL}{username}/graphs/{graph_id}"
    data = {"date": date, "quantity": quantity}
    response = make_pixela_request(endpoint, method="post", data=data, token=token)
    print(response.text)
    print(endpoint)

def update_pixel(username, token, graphs):
    """Updates an existing data point on a Pixela graph."""
    print("Available graphs:")
    print_graphs(graphs)
    graph_id = input("Enter graph ID: ")
    date = input("Enter date of the pixel to update (YYYYMMDD): ")
    quantity = input("Enter new quantity: ")
    endpoint = f"{PIXELA_BASE_URL}{username}/graphs/{graph_id}/{date}"
    data = {"quantity": quantity}
    response = make_pixela_request(endpoint, method="put", data=data, token=token)
    print(response.text)
    print(endpoint)

def delete_pixel(username, token, graphs):
    """Deletes a data point from a Pixela graph."""
    print("Available graphs:")
    print_graphs(graphs)
    graph_id = input("Enter graph ID: ")
    date = input("Enter date of the pixel to delete (YYYYMMDD): ")
    endpoint = f"{PIXELA_BASE_URL}{username}/graphs/{graph_id}/{date}"
    response = make_pixela_request(endpoint, method="delete", token=token)
    print(response.text)
    print(endpoint)

def login():
    """Prompts user for credentials and validates them."""
    username = input("Enter your username: ")
    token = input("Enter your Pixela token: ")
    hashed_token = get_hashed_token(token)
    login_endpoint = f"https://pixe.la/@{username}"
    headers = {"X-USER-TOKEN": hashed_token}
    response = requests.put(url=login_endpoint, headers=headers, json={"displayName": username})

    if response.status_code == 200:
        print("Login successful!")
        print(f"Welcome to Pixela! Visit {login_endpoint} to view your profile.")
        return username, token
    else:
        print(response.text)
        return None, None
