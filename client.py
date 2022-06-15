import requests


HOST = "http://127.0.0.1:5000/"


# method GET
def method_get(variable):
    resp = requests.get(f"{HOST}/api/{variable}")
    return resp.json()


# method POST
def method_post(json_data):
    requests.post(f"{HOST}/api/post", json=json_data)


# method DELETE
def method_del(variable):
    requests.delete(f"{HOST}/api/{variable}")


# method PATCH
def method_patch(variable, json_data):
    resp = requests.patch(f"{HOST}/api/{variable}", json=json_data)
    return resp.json()


#test

# advert = [{"title": "Garage",
#           "description": "Buy a garage",
#            "author": "Ivanov"},
#           {"title": "Desk",
#            "description": "Good condition",
#            "author": "Petrov"},
#           {"title": "Ryzen 5600x",
#            "description": "Like new",
#            "author": "Sidorov"},
#           ]
#
# for i in advert:
#     method_post(i)

# print(method_get(1))
# print(method_get(3))
# update_data = {"title": "headphone"}
# method_patch(3, update_data)
# print(method_get(3))
# method_del(2)
