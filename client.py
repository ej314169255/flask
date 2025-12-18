import requests

response = requests.post(
    "http://127.0.0.1:5000/users",
    json={"name": "user_3", "password": "123fafgasT#E#%R4"},
)
print(response.status_code)
print(response.json())


# response = requests.get("http://127.0.0.1:5000/users/20",)
# print(response.status_code)
# print(response.json())


# response = requests.patch("http://127.0.0.1:5000/users/2", json={
#     "name": "new_name"
# })
# print(response.status_code)
# print(response.json())

# response = requests.get("http://127.0.0.1:5000/users/2",)
# print(response.status_code)
# print(response.json())

# response = requests.delete("http://127.0.0.1:5000/users/2")
# print(response.status_code)
# print(response.json())


# response = requests.get("http://127.0.0.1:5000/users/2",)
# print(response.status_code)
# print(response.json())

# response = requests.delete("http://127.0.0.1:5000/users/20")
# print(response.status_code)
# print(response.json())
#
