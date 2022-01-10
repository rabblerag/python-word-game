import yaml
from yaml.loader import FullLoader

with open("test.yaml", "r") as f:
    users = yaml.load(f, Loader=FullLoader)
    print(users)
    newUsers = [users, {"name": "John", "age": 18}]
    print(newUsers)

with open("test.yaml", "w") as f:
    yaml.dump(newUsers, f)

with open("test.yaml", "r") as f:
    users = yaml.load(f, Loader=FullLoader)
    print(users)

