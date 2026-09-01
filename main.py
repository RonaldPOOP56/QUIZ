import json

with open("template.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data["100"]["questions"][0]["question"])
