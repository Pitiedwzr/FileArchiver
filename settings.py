import yaml

class commonClass:
    def __init__(self, raw):
        self.settings = raw
        self.language = raw['language']

class config:
    def __init__(self, raw):
        self.common = commonClass(raw['Common'])

with open("settings.yaml", "r") as f:
    config = config(yaml.safe_load(f))