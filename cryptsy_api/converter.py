# -*- coding: utf-8 -*-
from . import base

class ConverterApi(base.Api):
    _path = 'converter',

    def convert(self, item_id):
        return self._get(item_id)

    def convert_create(self, fromcurrency, tocurrency, sendingamount=0.0, receivingamount=0.0,
                       tradekey='', feepercent=0.0):
        return self._post(fromcurrency=fromcurrency, tocurrency=tocurrency,
                          sendingamount=sendingamount, receivingamount=receivingamount,
                          tradekey=tradekey, feepercent=feepercent)
