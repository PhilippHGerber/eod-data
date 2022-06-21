# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:13:31 2021

@author: lauta
"""

from eod.exchanges.bulk_eod_splits_divs_api import BulkMarketRequest
from eod.exchanges.list_tickers_api import ExchangesAndTickers
from eod.exchanges.trading_hours_market_holidays_api import MarketHoursHolidays
from eod.exchanges.search_instrument_api import SearchInstrument
from eod.exchanges.stock_market_screener_api import StockMarketScreener
from requests import Session


class ExchangesAndMarkets(BulkMarketRequest, ExchangesAndTickers, MarketHoursHolidays,
                          SearchInstrument, StockMarketScreener):
    def __init__(self, api_key:str, timeout:int, session: Session):
        BulkMarketRequest.__init__(self, api_key, timeout, session)
        ExchangesAndTickers.__init__(self, api_key, timeout, session)
        MarketHoursHolidays.__init__(self, api_key, timeout, session)
        SearchInstrument.__init__(self, api_key, timeout, session)
        StockMarketScreener.__init__(self, api_key, timeout, session)
