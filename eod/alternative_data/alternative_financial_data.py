from eod.alternative_data.sentiment_financial_api import SentimentFinancialData
from eod.alternative_data.financial_news_api import FinancialNews
from eod.alternative_data.macroeconomic_api import MacroEconomicIndicators
from eod.alternative_data.economic_events_data_api import EconomicEventsData
from requests import Session


class AlternativeFinancialDataEOD(SentimentFinancialData, FinancialNews,
                                  MacroEconomicIndicators, EconomicEventsData):
    def __init__(self, api_key:str, timeout:int, session: Session):
        SentimentFinancialData.__init__(self, api_key, timeout, session)
        FinancialNews.__init__(self, api_key, timeout, session)
        MacroEconomicIndicators.__init__(self, api_key, timeout, session)
        EconomicEventsData.__init__(self, api_key, timeout, session)