# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:06:37 2021

@author: lauta
"""

from requests import Session
from eod.exchanges import ExchangesAndMarkets
from eod.fundamental_economic_data import FundamentalEconomicData
from eod.historical_prices import HistoricalPrices


class EodHistoricalData(HistoricalPrices, FundamentalEconomicData, ExchangesAndMarkets):
    def __init__(self, api_key: str, timeout: int = 300, session: Session = None):
        # Substructures of the API
        HistoricalPrices.__init__(self, api_key, timeout, session)
        FundamentalEconomicData.__init__(self, api_key, timeout, session)
        ExchangesAndMarkets.__init__(self, api_key, timeout, session)
