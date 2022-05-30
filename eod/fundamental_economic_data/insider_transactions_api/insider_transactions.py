# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 18:50:39 2021

@author: lauta
"""

from eod.request_handler_class import RequestHandler
from requests import Session


class InsiderTransactions(RequestHandler):
    def __init__(self, api_key: str, timeout: int, session: Session):
        # base URL's of the API
        self.URL_INSIDER = 'https://eodhistoricaldata.com/api/insider-transactions'
        super().__init__(api_key, timeout, session)

    def get_insider_transactions(self, **query_params):
        self.endpoint = self.URL_INSIDER
        return super().handle_request(self.endpoint, query_params)
