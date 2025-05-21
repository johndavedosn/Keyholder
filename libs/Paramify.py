import json
from time import sleep
class ConfigFile:
    def __init__(self, file_name: str):
        self.file_name = file_name
        if ".json" not in file_name:
            raise ValueError("Sorry, but this module only supports json for now")
        with open(file_name, "r") as config_file:
            config = json.load(config_file)
        self.config: dict = config

    def load_param(self, param: str, default: str | None = None):
        if param in self.config:
            param_loaded = self.config[param]
            return param_loaded
        else:
            return default
    
    def list_parameters(self):
        return list(self.config.keys())
    
    def is_in_config(self, param: str):
        return param in self.config
    
    def update_param(self, param: str, value):
        if param in self.config:
            self.config[param] = value
            with open(self.file_name, "w") as config_file:
                json.dump(self.config, config_file, indent=2)
    def validate(self, param_name: str, expected_type):
        if param_name in self.config:
            param_value = self.config[param_name]
            if isinstance(param_value, expected_type):
                return True
        return False
class ConfigStream:
    def __init__(self, config_filename: str):
        self.config_file = config_filename

    def update_param(self, param: str, value):
        config_file = ConfigFile(self.config_file)
        config_file.update_param(param, value)
    def stream(self, param ,values: list, delay=0):
        config_file = ConfigFile(self.config_file)
        for value in values:
            config_file.update_param(param, value)
            sleep(delay)