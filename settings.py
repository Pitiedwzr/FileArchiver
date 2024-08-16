import yaml


# Use class to manage settings
class CommonConfig:
    # Set to the data that get from the raw data
    def __init__(self, raw):
        self.settings = raw

    # Use the key which passed here to find its value
    def __getattr__(self, item):
        return self.settings.get(item)

    # Save the key and value
    def __setattr__(self, key, value):
        if key == 'settings':
            super().__setattr__(key, value)
        else:
            self.settings[key] = value


class Config:
    # Initial data to class(es)
    def __init__(self, raw):
        self.common = CommonConfig(raw['Common'])

    # Save all changes of settings
    def save(self):
        data = {
            'Common': self.common.settings
        }
        with open("settings.yaml", 'w') as f:
            yaml.safe_dump(data, f)


# Load the configuration
with open("settings.yaml", "r") as f:
    config = Config(yaml.safe_load(f))
