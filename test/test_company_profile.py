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
from finnhub.models.company_profile import CompanyProfile  # noqa: E501
from finnhub.rest import ApiException

class TestCompanyProfile(unittest.TestCase):
    """CompanyProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CompanyProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = finnhub.models.company_profile.CompanyProfile()  # noqa: E501
        if include_optional :
            return CompanyProfile(
                address = '0', 
                city = '0', 
                country = '0', 
                currency = '0', 
                cusip = '0', 
                sedol = 56, 
                description = '0', 
                exchange = '0', 
                ggroup = '0', 
                gind = '0', 
                gsector = '0', 
                gsubind = '0', 
                isin = '0', 
                naics_national_industry = '0', 
                naics = '0', 
                naics_sector = '0', 
                naics_subsector = '0', 
                name = '0', 
                phone = '0', 
                state = '0', 
                ticker = '0', 
                weburl = '0', 
                ipo = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                market_capitalization = 1.337, 
                share_outstanding = 1.337, 
                employee_total = 56, 
                logo = '0', 
                finnhub_industry = '0'
            )
        else :
            return CompanyProfile(
        )

    def testCompanyProfile(self):
        """Test CompanyProfile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
