import yaml


class CommonConfig:
    """
    Represents common configuration settings.
    Provides attribute-like access to configuration items.
    """
    def __init__(self, raw):
        """Set to the data that get from the raw data"""
        self.settings = raw

    def __getattr__(self, item):
        """
        Allow attribute-like access to configuration items
        item is the configuration item to access
        return the value of the configuration item
        """
        return self.settings.get(item)
    
    def __setattr__(self, key, value):
        """
        Allow attribute-like setting of configuration items.
        key is the configuration item to set
        value is the value to save to the configuration item
        """
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
        with open("settings.yaml", 'w', encoding="utf-8") as yaml_data:
            yaml.safe_dump(data, yaml_data)


# Load the configuration
with open("settings.yaml", "r", encoding="utf-8") as setting_data:
    config = Config(yaml.safe_load(setting_data))
