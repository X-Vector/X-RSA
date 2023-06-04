# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import requests


ENDPOINT = "http://factordb.com/api"


class FactorDB():
    def __init__(self, n):
        self.n = n
        self.result = None

    def connect(self, reconnect=False):
        if self.result and not reconnect:
            return self.result
        self.result = requests.get(ENDPOINT, params={"query": str(self.n)})
        return self.result

    def get_id(self):
        return self.result.json().get("id") if self.result else None

    def get_status(self):
        return self.result.json().get("status") if self.result else None

    def get_factor_from_api(self):
        return self.result.json().get("factors") if self.result else None

    def get_factor_list(self):
        """
        get_factors: [['2', 3], ['3', 2]]
        Returns: [2, 2, 2, 3, 3]
        """
        factors = self.get_factor_from_api()
        if not factors:
            return []
        ml = [[int(x)] * y for x, y in factors]
        return [y for x in ml for y in x]

