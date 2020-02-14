from unittest import TestCase
from mock import patch  # for Python >= 3.3 use unittest.mock

from src.main.userfunctions.url_session import session_url


class FetchTests(TestCase):
    def test_returns_true_if_url_found(self):
        with patch('requests.get') as mock_request:
            url = 'http://google.com'
            mock_request.return_value.status_code = 200
            self.assertTrue(session_url(url))
            #mock_request.assert_called_once_with(url)

    def test_returns_false_if_url_not_found(self):
        with patch('requests.get') as mock_request:
            url = 'http://google.com/nonexistingurl'
            mock_request.return_value.status_code != 200
            self.assertTrue(session_url(url))
            #mock_request.assert_called_once_with(url)
