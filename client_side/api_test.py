import requests

BASE = "http://127.0.0.1:5000/api"

data = [
    {"name": "tim", "age": 40},
    {"name": "bill", "age": 18},
    {"name": "jill", "age": 26},
    {"name": "jack", "age": 20},
    {"name": "mac", "age": 72},
    {"name": "lucy", "age": 53}
]

print("PUT request")
for i in range(len(data)):
    response = requests.put(BASE + str(i+1), data[i])
    print(response.json())

print()
print("GET request")
response = requests.get(BASE + "1")
print(response.json())

print(BASE)
