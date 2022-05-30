import socket
import time
from typing import Dict
from urllib.parse import urlencode

import requests
from requests import Session


class RequestHandler():
    def __init__(self, api_key: str, timeout: int, session: Session = None, max_retries: int = 3):
        # general parameters of the api
        self.api_key = api_key
        self.timeout = timeout
        self.resp = None
        self.session = session
        self.max_retries = max_retries
        self.rate_limit_remaining = 2000
        self.last_request_time = 0

    # -------------------------------------------
    # Methods for data processing
    # -------------------------------------------

    def handle_request(self, endpoint_url, query_params: Dict[str, str] = {}):
        """
        central point to handle the requests of the API

        Parameters
        ----------
        session : requests.Session, optional
        query_params : Dict[str, str], optional
            query parameters of the request. The default is {}.

        Returns
        -------
        dict or list
            response from the API.

        """
        # append the api key and format to the parameters
        query_params_ = self.__append_fmt(query_params)

        for _ in range(self.max_retries):
            try:
                if (self.rate_limit_remaining < 10) and ((time.time() - self.last_request_time) < 60):
                    time.sleep(60 - (time.time() - self.last_request_time))

                if self.session is None:
                    self.resp = requests.get(url=endpoint_url, params=query_params_, timeout=self.timeout)
                else:
                    self.resp = self.session.get(url=endpoint_url, params=query_params_, timeout=self.timeout)

                self.last_request_time = time.time()
                self.rate_limit_remaining = int(self.resp.headers['X-RateLimit-Remaining'])
                break

            except socket.timeout:
                print("URL that generated the error code: ", endpoint_url)
                print("Error description: No response.")
            except socket.error:
                print("URL that generated the error code: ", endpoint_url)
                print("Error description: Socket error.")

        if self.resp.status_code == 200:
            return self.resp.json()
        else:
            self.resp.raise_for_status()

    def __append_fmt(self, dict_to_append):
        """
        Append the type of format and api key to the query parameters

        Parameters
        ----------
        dict_to_append : dict
            paramters of the request.

        Returns
        -------
        dict_to_append : dict
            full dict of paramters of the request.

        """
        dict_to_append['fmt'] = 'json'
        dict_to_append['api_token'] = self.api_key

        # from query parameter
        if 'from' in dict_to_append:
            del dict_to_append['from']

        if 'from_' in dict_to_append:
            dict_to_append['from'] = dict_to_append.pop('from_')

        # type query parameter
        if 'type' in dict_to_append:
            del dict_to_append['type']

        if 'type_' in dict_to_append:
            dict_to_append['type'] = dict_to_append.pop('type_')

        # filter query parameter
        if 'filter' in dict_to_append:
            del dict_to_append['filter']

        if 'filter_' in dict_to_append:
            dict_to_append['filter'] = dict_to_append.pop('filter_')

        return dict_to_append
