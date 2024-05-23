import yaml

class commonConfig:
    def __init__(self, raw):
        self.settings = raw

    def __getattr__(self, item):
        return self.settings.get(item)

    def __setattr__(self, key, value):
        if key == 'settings':
            super().__setattr__(key, value)
        else:
            self.settings[key] = value

class config:
    def __init__(self, raw):
        self.common = commonConfig(raw['Common'])

    def save(self):
        data = {
            'Common': self.common.settings
        }
        with open("settings.yaml", 'w') as f:
            yaml.safe_dump(data, f)

# Load the configuration
with open("settings.yaml", "r") as f:
    config = config(yaml.safe_load(f))