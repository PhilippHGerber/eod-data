# -*- coding: utf-8 -*-
"""
Created on Mon May 10 10:00:38 2021

@author: lauta
"""

from eod.fundamental_economic_data.fundamental_api import StockEtfFundsIndexFundamentalData
from eod.fundamental_economic_data.calendar_earnings_trends_ipos_splits_api import CalendarEarningsTrendsIposSplits
from eod.fundamental_economic_data.insider_transactions_api import InsiderTransactions
from eod.fundamental_economic_data.historical_market_capitalization_api import HistoricalMarketCapitalization
from requests import Session

class FundamentalEconomicData(StockEtfFundsIndexFundamentalData, CalendarEarningsTrendsIposSplits,
                              InsiderTransactions, HistoricalMarketCapitalization):
    def __init__(self, api_key:str, timeout:int, session: Session):
        # inhereting the API classes
        StockEtfFundsIndexFundamentalData.__init__(self, api_key, timeout, session)
        CalendarEarningsTrendsIposSplits.__init__(self, api_key, timeout, session)
        InsiderTransactions.__init__(self, api_key, timeout, session)
        HistoricalMarketCapitalization.__init__(self, api_key, timeout, session)
