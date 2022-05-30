# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:28:22 2022

@author: lauta
"""

from requests import Session
from eod.request_handler_class import RequestHandler


class EconomicEventsData(RequestHandler):
    def __init__(self, api_key: str, timeout: int, session: Session):
        # base URL's of the API
        self.URL_ECONOMIC_EVENT_DATA = 'https://eodhistoricaldata.com/api/economic-events/'
        super().__init__(api_key, timeout, session)

    def get_economic_events(self, **query_params):
        self.endpoint = self.URL_ECONOMIC_EVENT_DATA
        return super().handle_request(self.endpoint, query_params)
