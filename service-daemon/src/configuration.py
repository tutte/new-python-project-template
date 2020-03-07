
import os

class ConfigHandler():
    def __init__(self):
        from config import default_config
        self._cfg = default_config
        self._cfg = self.getEnvOverrides()

    def getEnvOverrides(self):
        cfg = self._cfg
        cfg['name'] = os.getenv('APP_NAME', cfg['name'])
        cfg['log_level'] = os.getenv('LOG_LEVEL', cfg['log_level'])
        return cfg

    def __getattr__(self, attribute):
        return self._cfg.get(attribute)

config = ConfigHandler()
