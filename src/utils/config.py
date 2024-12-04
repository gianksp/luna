import json

config_data = None

with open("config.json") as json_data_file:
    config_data = json.load(json_data_file)

def get(key):
    return config_data[key]
