import requests
def get_token():
    url = "https://restful-booker.herokuapp.com/auth"

    data = {
        "username" : "admin",
        "password" : "password123"
    }
    CreateUser = requests.post(url, json=data)
    print(CreateUser.status_code)
    print(CreateUser.json())