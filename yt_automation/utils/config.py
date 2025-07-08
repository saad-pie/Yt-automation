import json

class Config:
    def __init__(self, config_path="config/config.json"):
        with open(config_path) as f:
            self.data = json.load(f)

    def get_openai_config(self):
        return self.data.get("openai", {})

    def get_script_config(self):
        return self.data.get("script", {})
