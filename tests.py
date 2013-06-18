import unittest

from httpretty import HTTPretty
from httpretty import httprettified

from contactology import Contactology


API_KEY = "abcdefghijklmnop"

RESPONSE_500 = 'Internal Server Error'
RESPONSE_200 = '{"foo":"bar"}'


class ContactologyTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Contactology(API_KEY)


class TestContact_Import(ContactologyTestCase):
    @httprettified
    def test_500(self):
        HTTPretty.register_uri(HTTPretty.POST,
                               'http://api.emailcampaigns.net/2/REST/',
                               status=500, body=RESPONSE_500)
        self.assertRaises(Exception, self.client.Contact_Import, [], 'Foobar')

    @httprettified
    def test_200(self):
        HTTPretty.register_uri(HTTPretty.POST,
                               'http://api.emailcampaigns.net/2/REST/',
                               status=200, body=RESPONSE_200)
        r = self.client.Contact_Import([], 'Foobar')


if __name__ == '__main__':
    unittest.main()
