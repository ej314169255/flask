import requests

# response = requests.post(
#     "http://127.0.0.1:5000/records",
#     json={"title": "shoes", "descr": "like fast new", "owner": "big Mazzy", "status": "ski"}
# )
# print(response.status_code)
# print(response.json())


# response = requests.patch("http://127.0.0.1:5000/records/7", json={
#     "title": "A pair of shoes"
# })
# print(response.status_code)
# print(response.json())

response = requests.get("http://127.0.0.1:5000/records/9",)
print(response.status_code)
print(response.json())

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
