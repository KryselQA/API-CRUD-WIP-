import requests
def get_token():
    url = "https://restful-booker.herokuapp.com/auth"

    data = {
        "username" : "admin",
        "password" : "password123"
    }
    create_user = requests.post(url, json=data)
    print(create_user.status_code)
    print(create_user.json())