import yaml


# Represents common configuration settings.
# Provides attribute-like access to configuration items.
class CommonConfig:
    # Set to the data that get from the raw data
    def __init__(self, raw):
        self.settings = raw

    # Allow attribute-like access to configuration items
    # item is the configuration item to access
    # return the value of the configuration item
    def __getattr__(self, item):
        return self.settings.get(item)

    # Allow attribute-like setting of configuration items.
    # key is the configuration item to set
    # value is the value to save to the configuration item
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
