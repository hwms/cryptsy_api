# -*- coding: utf-8 -*-
from . import base

class OldPublicApi(base.Api):

    def _request(self, *args, **kwargs):
        kwargs = dict(dict(url=self.config.old_public_url, signed=False), **kwargs)
        return super()._request(*args, **kwargs)

    def _public_get(self, method, marketid=None):
        return super()._public_get(method=method, marketid=marketid)

    def marketdata(self):
        """General Market Data (All Markets - Delayed up to 1 minute).
        :return: Dict of dicts of active markets data with orders.
            {'markets': {label: marketdata, ..}}.
            marketdata (dict):
                marketid:       Integer value representing a market
                label:          Name for this market. Example: AMC/BTC
                primarycode:    Primary currency code. Example: AMC
                primaryname:    Primary currency name. Example: AmericanCoin
                secondarycode:  Secondary currency code. Example: BTC
                secondaryname:  Secondary currency name. Example: BitCoin
                volume:         24 hour trading volume in this market
                lasttradeprice: Last trade price for this market
                lasttradetime:  Last trade time for this market
                sellorders:     [order, ..]
                buyorders:      [order, ..]
                recenttrades:   [trade, ..]
            order (dict):
                total, price, quantity
            trade (dict):
                id, type, time, total, price, quantity
        """
        return self._public_get('marketdatav2')

    def singlemarketdata(self, marketid):
        """General Market Data (Single Market - Realtime).
        :return: Dict of dicts of active markets data with orders only for selected market.
            {'markets': {label: marketdata, ..}}.
            marketdata (dict):
                marketid:       Integer value representing a market
                label:          Name for this market. Example: AMC/BTC
                primarycode:    Primary currency code. Example: AMC
                primaryname:    Primary currency name. Example: AmericanCoin
                secondarycode:  Secondary currency code. Example: BTC
                secondaryname:  Secondary currency name. Example: BitCoin
                volume:         24 hour trading volume in this market
                lasttradeprice: Last trade price for this market
                lasttradetime:  Last trade time for this market
                sellorders:     [order, ..]
                buyorders:      [order, ..]
                recenttrades:   [trade, ..]
            order (dict):
                total, price, quantity
            trade (dict):
                id, type, time, total, price, quantity
        """
        return self._public_get('singlemarketdata', marketid)

    def orderdata(self):
        """General Orderbook Data (All Markets - Delayed up to 1 minute).
        :return: Dict of dicts of all orders from all markets.
            {label: orderdata, ..}}.
            orderdata (dict):
                marketid:       Integer value representing a market
                label:          Name for this market. Example: AMC/BTC
                primarycode:    Primary currency code. Example: AMC
                primaryname:    Primary currency name. Example: AmericanCoin
                secondarycode:  Secondary currency code. Example: BTC
                secondaryname:  Secondary currency name. Example: BitCoin
                sellorders:     [order, ..]
                buyorders:      [order, ..]
            order (dict):
                total, price, quantity
        """
        return self._public_get('orderdatav2')

    def singleorderdata(self, marketid):
        """ General Orderbook Data (Single Market - Realtime)
        :return: Dict of dicts of all orders only for selected market.
            {label: orderdata, ..}}.
            orderdata (dict):
                marketid:       Integer value representing a market
                label:          Name for this market. Example: AMC/BTC
                primarycode:    Primary currency code. Example: AMC
                primaryname:    Primary currency name. Example: AmericanCoin
                secondarycode:  Secondary currency code. Example: BTC
                secondaryname:  Secondary currency name. Example: BitCoin
                sellorders:     [order, ..]
                buyorders:      [order, ..]
            order (dict):
                total, price, quantity
        """
        return self._public_get('singleorderdata', marketid)
