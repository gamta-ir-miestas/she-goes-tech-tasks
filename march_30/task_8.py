# Write a Python program that reads a JSON file 
# containing a list of dictionaries, sorts the list by 
# a specific key, and writes the sorted list back to 
# the file.

import json

with open("example.json", "r") as f:
    data = json.load(f)

sortt = sorted(data, key = lambda x: x['banana'])

with open("output.json", "w") as f:
    json.dump(sortt, f)