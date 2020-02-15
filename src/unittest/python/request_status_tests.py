# import unittest
from unittest import TestCase
from mock import patch  # for Python >= 3.3 use unittest.mock


from src.unittest.python.url_session_tests import session_url


class FetchTests(TestCase):
    def test_returns_true_if_url_found(self):
        with patch('requests.get') as mock_request:
            url = 'http://google.com'
            mock_request.return_value.status_code = 200
            self.assertTrue(session_url(url))
            #mock_request.assert_called_once_with(url)
