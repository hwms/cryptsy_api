# -*- coding: utf-8 -*-
from . import base

class TriggerApi(base.Api):
    _path = 'trigger',

    def __call__(self, trigger_id=None):
        """List currency info for a currency/currencies - Authenticated.
        :param currency_id: (optional) Currency id.
        :return: Dict(s) for a currency/currencies:
            id (str):          Currency id as integer string.
            code (str):        Code for the currency, eg. LTC.
            name (str):        Name for the currency, eg. LiteCoin.
            maintenance (str): Maintence mode as integer string (0 - No issues, 1 - Maintenance,
                               2 - Updating wallet, 3 - Network issues).
        """
        return self._get(trigger_id)

    def create(self, market_id, ordertype, quantity, comparison, price, orderprice, expires=''):
        return self._post(market_id=market_id, type=ordertype, quantity=quantity,
                          comparison=comparison, price=price, orderprice=orderprice,
                          expires=expires)

    def remove(self, trigger_id):
        return self._delete(trigger_id)
