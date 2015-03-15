# -*- coding: utf-8 -*-
import logging
from decimal import Decimal

log = logging.getLogger(__name__)

def get_first(dct, *keys, not_value=None, default=None):
    for value in (dct.get(k, not_value) for k in keys):
        if value is not not_value:
            return value
    return default

def coerce_choice(value, choices):
    return value if value in choices else choices[0]

class Trigger(RestResourceBase):

    TYPES = ('sell', 'buy')
    COMPARISONS = ('<=', '=>', 'lteg', 'gteq')

    def __init__(self, api, market_id=None, market=None, order_type=None, comparison=None, **kwargs):
        self.api = api
        self.market_id = get_first(kwargs, 'marketid', 'market_id')
        self.type = coerce_choice(kwargs.get('type', '').lower(), Trigger.TYPES)
        self.comparison = coerce_choice(kwargs.get('comparison', '').lower(), Trigger.COMPARISONS)
        self.quantity = Decimal(kwargs.get('quantity', 0))
        self.price = Decimal(kwargs.get('price', 0))
        self.orderprice = Decimal(kwargs.get('orderprice', 0))
        self.expires = kwargs.get('expires', None)

class TriggerManager(RestResourceBase):
    method = 'trigger'
    cls = Trigger

    def __init__(self, api):
        self.api = api
        self._cache = {}

    def sync(self):
        success, results = self.query()
        if not success:
            raise ValueError(results)
        for result in results:
            obj = self.cls(**result)
            self._cache[obj.id] = obj

    def get(self, obj_id):
        if not self._cache:
            self.sync()
        return self._cache[obj_id]
    __getitem__ = get

    def __iter__(self):
        if not self._cache:
            self.sync()
        return iter(self._cache.values())

