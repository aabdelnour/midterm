import importlib
import os

class PluginManager:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                module = importlib.import_module(f"{self.plugin_dir}.{module_name}")
                self.plugins[module_name] = module

    def get_plugins(self):
        return self.plugins
