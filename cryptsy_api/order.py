# -*- coding: utf-8 -*-
from . import base

class OrderApi(base.Api):
    _path = 'order',

    def __call__(self, order_id):
        """List order info - Authenticated.
        :param order_id: (optional) Currency id.
        :return: Dict with infos for the order::
            orderinfo (dict):  Order infos:
                remainqty (float): Remaining quantity in coin currency, eg. LTC.
                active (bool):     The order is still active.
            tradeinfo (dicts): Trade infos:
                ?
        """
        return self._get(order_id)

    def create(self, market_id, quantity, order_type, price):
        """Create an order - Authenticated.
        :param market_id:         Market id.
        :param quantity (float):  Quantity to order in coin currency, eg. LTC.
        :param order_type (str):  Type of order: buy/sell.
        :param price (float):     Price in market currency, eg. USD.
        :return: Dict containing the order id of the created order.
            orderid (str):  Order id as integer string.
            moreinfo (str): HTML info about the order creation
        """
        return self._post(quantity=quantity, ordertype=order_type, price=price, marketid=market_id)

    def delete(self, order_id):
        """Delete an order - Authenticated.
        :param order_id: Order id.
        :return: ?
        """
        return self._delete(order_id)
