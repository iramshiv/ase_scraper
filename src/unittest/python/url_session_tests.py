import unittest

from src.main.python.url_session import session_url


class SessionUrlTest(unittest.TestCase):

    def test_correct_message(self):
        url = 'http://google.com/'
        self.assertTrue(session_url(url), 200)


if __name__ == '__main__':
    unittest.main()