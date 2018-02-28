import json


with open("data\\bosses.json") as f:
    d = json.load(f)
    print(d["boss1"])
