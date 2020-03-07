import src
import os
import unittest
from unittest import mock

class TestConfig(unittest.TestCase):
    def test_defaults_uses_config(self):
        self.assertEqual(src.config.name, 'test_service')
        self.assertEqual(src.config.log_level, 'ERROR')

class TestConfigEnvOverrides(unittest.TestCase):
    environ_overrides = {
        'APP_NAME': 'name_test',
        'LOG_LEVEL': 'DEBUG'
    }
    def setUp(self):
        import importlib
        with mock.patch.dict('os.environ', self.environ_overrides):
            importlib.reload(src.configuration)
            importlib.reload(src)

    def test_config_overrides_name_env(self):
        self.assertEqual(src.config.name, 'name_test')
            
    def test_config_overrides_log_env(self):
        import logging
        self.assertEqual(src.config.log_level, 'DEBUG')
        self.assertEqual(src.log.level, logging.DEBUG)
