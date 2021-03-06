# coding: utf-8

"""
    Finnhub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import finnhub
from finnhub.models.earning_release import EarningRelease  # noqa: E501
from finnhub.rest import ApiException

class TestEarningRelease(unittest.TestCase):
    """EarningRelease unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EarningRelease
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = finnhub.models.earning_release.EarningRelease()  # noqa: E501
        if include_optional :
            return EarningRelease(
                symbol = '0', 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                hour = '0', 
                year = 56, 
                quarter = 56, 
                eps_estimate = 1.337, 
                eps_actual = 1.337, 
                revenue_estimate = 56, 
                revenue_actual = 56
            )
        else :
            return EarningRelease(
        )

    def testEarningRelease(self):
        """Test EarningRelease"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
