import requests
def get_token():
    url = "https://restful-booker.herokuapp.com/auth"

    data = {
        "username" : "admin",
        "password" : "password123"
    }
    create_user = requests.post(url, json=data)
    token = create_user.json()["token"]
    return create_user.status_code, create_user.json(), token