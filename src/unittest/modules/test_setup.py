from unittest.mock import patch
import uuid

from ..base import BaseTest
from ...modules import setup


class Test(BaseTest):

    def test_setup(self):
        with patch('getpass.getpass', return_value=str(uuid.uuid4())):
            self.assertTrue(setup.initialize(self.config.getConfig()['salt']))

    def test_create_db(self):
        self.assertTrue(setup.create_db())

    def test_get_key_input(self):
        with patch('getpass.getpass', return_value=str(uuid.uuid4())):
            self.assertTrue(setup.get_key_input())

    def test_get_key_input_2(self):
        with patch('getpass.getpass', return_value='abc'):
            self.assertFalse(setup.get_key_input())

    def test_is_key_valid(self):
        self.assertTrue(setup.is_key_valid('some_valid_key_123'))

    def test_is_key_valid_2(self):
        self.assertFalse(setup.is_key_valid('abc'))

    def test_check_key_and_repeat(self):
        self.assertTrue(setup.check_key_and_repeat(
            'some_valid_key_123', 'some_valid_key_123'))

    def test_check_key_and_repeat_2(self):
        self.assertFalse(setup.check_key_and_repeat(
            'some_valid_key_123', 'some_valid_key_123456'))
