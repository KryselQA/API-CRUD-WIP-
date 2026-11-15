import requests

url = "https://restful-booker.herokuapp.com/auth"

data = {
    "username" : "admin",
    "password" : "password123"
}
#Пустой коммент для коммита
CreateUser = requests.post(url, json=data)
print(CreateUser.status_code)
print(CreateUser.json())