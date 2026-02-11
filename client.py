import requests

# response = requests.post(
#     "http://127.0.0.1:5000/users",
#     json={"name": "user_3", "password": "123fafgasT#E#%R4"},
# )
# print(response.status_code)
# print(response.json())

# response = requests.post('http://127.0.0.1:5000/hello/world/42?key1=val1&key2=val2',
#             json={"some": "data"},
#             headers={"Authorisation": "token"}
#         )
# print(response.status_code)
# print(response.json())

# response = requests.post(
#     "http://127.0.0.1:5000/records",
#     json={"descr": "Minimal length of description is 16", "owner": "Jimmy"}
# )
# print(response.status_code)
# print(response.json())


response = requests.patch("http://127.0.0.1:5000/records/20", json={"owner": "ex",
    "title": "A pair", "descr": "vMinimal length of description is 16", 
})
print(response.status_code)
print(response.json())

# response = requests.get("http://127.0.0.1:5000/records/20",)
# print(response.status_code)
# print(response.json())

# response = requests.delete("http://127.0.0.1:5000/records/10",
# json={"message": "deleted"}
# )
# print(response.status_code)
# print(response.json)

# response = requests.get("http://127.0.0.1:5000/users/2",)
# print(response.status_code)
# print(response.json())

# response = requests.delete("http://127.0.0.1:5000/users/20")
# print(response.status_code)
# print(response.json())
#
