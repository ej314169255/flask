import requests

# response = requests.post(
#     "http://127.0.0.1:5000/users",
#     json={"name": "user_3", "password": "123fafgasT#E#%R4"},
# )
# print(response.status_code)
# print(response.json())


# response = requests.post(
#     "http://127.0.0.1:5000/records",
#     json={"title": "shoes", "descr": "Minimal length of description is 16", "owner": "Jimmy"}
# )
# print(response.status_code)
# print(response.json())


# response = requests.patch("http://127.0.0.1:5000/records/18", json={
#     "title": "A pair of shoes now", "descr": "Minimal length of description is 16", "owner": "Smart"
# })
# print(response.status_code)
# print(response.json())

# response = requests.get("http://127.0.0.1:5000/records/18",)
# print(response.status_code)
# print(response.json())

response = requests.delete("http://127.0.0.1:5000/records/2",
json={"message": "deleted"}
)
print(response.status_code)
print(response.json)

# response = requests.get("http://127.0.0.1:5000/users/2",)
# print(response.status_code)
# print(response.json())

# response = requests.delete("http://127.0.0.1:5000/users/20")
# print(response.status_code)
# print(response.json())
#
