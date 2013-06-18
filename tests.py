import unittest

from functools import wraps

from httpretty import HTTPretty
from httpretty import httprettified as basehttprettified

from contactology import Contactology


API_KEY = 'abcdefghijklmnop'
API_URL = 'http://api.emailcampaigns.net/2/REST/'

RESPONSE_500 = 'Internal Server Error'
RESPONSE_200 = '{"foo":"bar"}'


def httprettified(status, body):
    """Since all API calls hit the same URL using POST, roll the URI
    registration into the decorator."""
    def wrapper(f):
        @wraps(f)
        def inner(*args, **kwargs):
            HTTPretty.register_uri(HTTPretty.POST, API_URL, status=status,
                                   body=body)
            return f(*args, **kwargs)
        return basehttprettified(inner)
    return wrapper


class ContactologyTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Contactology(API_KEY)


class TestContact_Import(ContactologyTestCase):
    @httprettified(500, RESPONSE_500)
    def test_500(self):
        self.assertRaises(Exception, self.client.Contact_Import, [], 'Foobar')

    @httprettified(200, RESPONSE_200)
    def test_200(self):
        r = self.client.Contact_Import([], 'Foobar')


if __name__ == '__main__':
    unittest.main()
