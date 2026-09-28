empty_dict = {}
empty_dict_alt = dict()

# creating with initial data
user = {
    "username": "coder123",
    "email": "coder123@example.com",
    "role": "developer",
    "login_count": 5
}


# 2. Creating from a list of tuples
pairs = [("status", "active"), ("verified", True)]
status_dict = dict(pairs)


# 3. Accessing values
role=user["role"]
# safer to execute
theme=user.get("theme","dark") #using dark as defualt value

#Adding and modifying elements
user["status"]="active"
user["login_count"]=6

# updating multiple items at once using another dictionary
user.update({"role":"senior_developer","location":"Remote"})



# 4.Removing other elements

# removing the specify key and returning its value
removed_role=user.pop("role")
removed_theme=user.pop("theme","light"); #provided a default fallback 

#remove the last item and returns the tuple: (key, value)
last_item=user.popitem()

# user.clear() #to clear the dict


# 5. Checking existence
if "username" in user:
    print("Username exist")


# 6. Dictionary views & iterations

#return a view object
all_keys=user.keys();
all_values=user.values();
all_items=user.items();   #getting key value pairs as tuple


for key in user:
    print(f"Key: {key}")


for value in user.values:
    print(f"Value: {value}")

for key,value in user.items():
    print(f"{key}: {value}")



# 7. utilites
num_properties=len(user)

# merging 2 dictionaries
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 3, "z": 4}
merged_dict = dict_a | dict_b  #dict b overrides dict a