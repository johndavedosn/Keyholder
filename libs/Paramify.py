import json
from time import sleep
class LogicalParam:
    def __init__(self, param):
        self.param = param

    def bind(self, func):
        if self.param:
            func()
    def get_value(self):
        return self.param

class ConfigFile:
    def __init__(self, file):
        self.file = file
        if ".json" not in file:
            raise ValueError("Sorry, but this module only supports json for now")
        with open(file, "r") as config_file:
            config = json.load(config_file)
        self.config = config

    def load_param(self, param, type, default=None):
        if param in self.config:
            param_loaded = self.config[param]
            if type == "log":
                return LogicalParam(param_loaded)
            else:
                return param_loaded
        else:
            return default
    
    def list_parameters(self):
        return list(self.config.keys())
    
    def is_in_config(self, param):
        return param in self.config
    
    def update_param(self, param, value):
        if param in self.config:
            self.config[param] = value
            with open(self.file, "w") as config_file:
                json.dump(self.config, config_file, indent=2)
    def validate(self, param_name, expected_type):
        if param_name in self.config:
            param_value = self.config[param_name]
            if isinstance(param_value, expected_type):
                return True
        return False
class ConfigStream:
    def __init__(self, config_file):
        self.config_file = config_file

    def update_param(self, param, value):
        config_file = ConfigFile(self.config_file)
        config_file.update_param(param, value)
    def stream(self, param ,values, delay=0):
        config_file = ConfigFile(self.config_file)
        for value in values:
            config_file.update_param(param, value)
            sleep(delay)
