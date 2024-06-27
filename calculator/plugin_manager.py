import importlib
import os
import logging

logger = logging.getLogger(__name__)

class PluginManager:
    def __init__(self, plugins_directory='plugins'):
        self.plugins_directory = plugins_directory
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        if not os.path.exists(self.plugins_directory):
            os.makedirs(self.plugins_directory)
        
        for filename in os.listdir(self.plugins_directory):
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(f'{self.plugins_directory}.{module_name}')
                    self.plugins[module_name] = module
                    logger.info(f'Loaded plugin: {module_name}')
                except ImportError as e:
                    logger.error(f'Error loading plugin {module_name}: {e}')

    def get_plugin(self, plugin_name):
        return self.plugins.get(plugin_name)
