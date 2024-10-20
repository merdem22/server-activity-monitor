import json

def load_servers(config_file="condig/servers.json"):
    with open(config_file, "r") as f:
        return json.load(f)