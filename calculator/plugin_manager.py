class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load_plugin(self, plugin):
        self.plugins[plugin.name] = plugin

    def get_plugin(self, name):
        return self.plugins.get(name, None)
    