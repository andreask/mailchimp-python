# coding=utf-8
import unittest

from mailchimp.config import Config


class TestConfig(unittest.TestCase):
    def test_base_url(self):
        config = Config()
        self.assertEqual("https://api.mailchimp.com/3.0", config.base_api_url)
        self.assertEqual("https://us1.api.mailchimp.com/3.0", config.get_server_url())

    def test_base_url_with_api_key(self):
        config = Config()
        config.api_key = "34672834678234-us1"
        self.assertEqual("https://api.mailchimp.com/3.0", config.base_api_url)
        self.assertEqual("https://us1.api.mailchimp.com/3.0", config.get_server_url())

    def test_base_url_with_other_dc_api_key(self):
        config = Config()
        config.api_key = "34672834678234-us6"
        self.assertEqual("https://api.mailchimp.com/3.0", config.base_api_url)
        self.assertEqual("https://us6.api.mailchimp.com/3.0", config.get_server_url())
