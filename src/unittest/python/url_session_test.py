from mockito import mock, verify, when, unstub
import unittest
import requests

from src.main.userfunctions.url_session import session_url


class SessionUrlTest(unittest.TestCase):

    def test_correct_message(self):
        url = 'http://google.com/'
        self.assertTrue(session_url(url), 200)
