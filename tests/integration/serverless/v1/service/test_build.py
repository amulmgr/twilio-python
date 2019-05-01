# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class BuildTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .builds.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Builds',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "builds": [],
                "meta": {
                    "first_page_url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Builds?PageSize=50&Page=0",
                    "key": "builds",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Builds?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .builds.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .builds(sid="ZBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Builds/ZBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "ZB00000000000000000000000000000000",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ZS00000000000000000000000000000000",
                "asset_versions": [
                    {
                        "sid": "ZN00000000000000000000000000000000",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ZS00000000000000000000000000000000",
                        "asset_sid": "ZH00000000000000000000000000000000",
                        "date_created": "2018-11-10T20:00:00Z",
                        "path": "asset-path",
                        "visibility": "PUBLIC"
                    }
                ],
                "function_versions": [
                    {
                        "sid": "ZN00000000000000000000000000000001",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ZS00000000000000000000000000000000",
                        "function_sid": "ZH00000000000000000000000000000001",
                        "date_created": "2018-11-10T20:00:00Z",
                        "path": "function-path",
                        "visibility": "PUBLIC"
                    }
                ],
                "dependencies": [
                    {
                        "name": "twilio",
                        "version": "3.6.3"
                    }
                ],
                "status": "deploying",
                "date_created": "2018-11-10T20:00:00Z",
                "date_updated": "2018-11-10T20:00:00Z",
                "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Builds/ZB00000000000000000000000000000000"
            }
            '''
        ))

        actual = self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .builds(sid="ZBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .builds.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Builds',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "ZB00000000000000000000000000000000",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ZS00000000000000000000000000000000",
                "asset_versions": [
                    {
                        "sid": "ZN00000000000000000000000000000000",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ZS00000000000000000000000000000000",
                        "asset_sid": "ZH00000000000000000000000000000000",
                        "date_created": "2018-11-10T20:00:00Z",
                        "path": "asset-path",
                        "visibility": "PUBLIC"
                    }
                ],
                "function_versions": [
                    {
                        "sid": "ZN00000000000000000000000000000001",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ZS00000000000000000000000000000000",
                        "function_sid": "ZH00000000000000000000000000000001",
                        "date_created": "2018-11-10T20:00:00Z",
                        "path": "function-path",
                        "visibility": "PUBLIC"
                    }
                ],
                "dependencies": [
                    {
                        "name": "twilio",
                        "version": "3.6.3"
                    }
                ],
                "status": "building",
                "date_created": "2018-11-10T20:00:00Z",
                "date_updated": "2018-11-10T20:00:00Z",
                "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Builds/ZB00000000000000000000000000000000"
            }
            '''
        ))

        actual = self.client.serverless.v1.services(sid="ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .builds.create()

        self.assertIsNotNone(actual)
