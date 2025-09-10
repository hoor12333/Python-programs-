import json

person = {"name": "Alice", "age": 25, "city": "New York"}

# Convert dictionary -> JSON string
json_str = json.dumps(person, indent=4)
print(json_str)

# Convert JSON string -> dictionary
parsed = json.loads(json_str)
print(parsed["name"], parsed["age"])
