# -*- coding: utf-8 -*-
from . import base

class MarketsApi(base.Api):
    _path = 'markets',

    def __call__(self, market_id=None):
        """List market info for (a) active market(s) - Unauthenticated.
        :param market_id: (optional) Market id.
        :return: Dict(s) for (a) market(s):
            id (str):                 Market id as integer string.
            label (str):              Name for this market, eg. LTC/USD.
            coin_currency_id (str):   Coin currency as integer string, eg: 2.
            market_currency_id (str): Market currency as integer string, eg: 1.
            maintenance_mode (str):   Maintence mode as integer string (0 - No issues,
                                      1 - Maintenance, 2 - Updating wallet, 3 - Network issues).
            verifiedonly (bool):      Verified account is needed to Trade on the market.
            last_trade (dict):        Last trade for this market:
                price (float):            Price in market currency (eg. USD).
                date (str):               Time as datetime string.
                timestamp (int):          Time as timestamp.
            24hr (dict):              24 hour aggregated trades.
                volume (float):           Volume in coin currency (eg. LTC).
                volume_btc (float):       Volume in BTC.
                price_high (float):       Highest price in market currency (eg. USD).
                price_low (float):        Lowest price in market currency (eg. USD).
        """
        return self._public_get(market_id)

    def volume(self, market_id=None):
        """List 24 hour volume for (a) market(s) - Unauthenticated.
        :param market_id: (optional) Market id.
        :return: Dict(s) for (a) market(s):
            id (str):           Market id as integer string.
            volume (float):     Volume in coin currency (eg. LTC).
            volume_btc (float): Volume in BTC.
        """
        return self._public_get(market_id, 'volume')

    def ticker(self, market_id=None):
        """List ticker for (a) market(s) - Unauthenticated.
        :param market_id: (optional) Market id.
        :return: Dict(s) for (a) market(s):
            id (str):    Market id as integer string.
            ask (float): Highest buy order price in market currency (eg. USD).
            bid (float): Lowest sell order price in market currency (eg. USD).
        """
        return self._public_get(market_id, 'ticker')

    def fees(self, market_id):
        """List your own fees active for the market - Authenticated.
        :param market_id: Market id.
        :return: Dict for a market:
            buyfeepercent (float):  Fee as percentage for buy orders.
            sellfeepercent (float): Fee as percentage for sell orders.
        """
        return self.query(market_id, 'fees')

    def triggers(self, market_id, limit=None):
        """List your own triggers active for the market - Authenticated.
        :param market_id: Market id.
        :param int limit: (optional) Limit return size: 0-100, default: 100.
        :return: Dict(s) for (a) market(s).
            triggerid (str):          Trigger id as integer string.
            action (str):             Order type: Buy/Sell.
            comparison (str):         Comparison sign (<= or =>), eg. for "When coin price <=".
            trigger_price (float):    Coin price to trigger in market currency (eg. USD).
            orderprice (float):       Order price to make in market currency (eg. USD).
            trigger_quantity (float): Maximum quantity to trade in coin currency (eg. LTC).
            expires (str):            Expire time as datetime string.
            expires_timestamp (int):  Expire time as timestamp.
        """
        return self.query(market_id, 'triggers', limit=limit)

    def orderbook(self, market_id, limit=None, order_type=None, mine=None):
        """List orderbook for the market - Unauthenticated.
        :param market_id:      Market id.
        :param int limit:      (optional) Limit return size: 0-100, default: 100.
        :param str order_type: (optional) Type of orders to query: Buy, Sell, Both, default: Both.
        :param bool mine:      (optional) Include my orders, default False.
        :return: Dict with order dicts (sellorders and/or buyorders depending on order_type):
            price (float):    Price in market currency (eg. USD).
            quantity (float): Quantity in coin currency (eg. LTC).
            total (float):    Total in market currency (eg. USD).
        """
        return self._public_get(market_id, 'orderbook', limit=limit, type=order_type, mine=mine)

    def tradehistory(self, market_id, limit=None, mine=None, start=None, stop=None):
        """List tradehistory for the market - Unauthenticated.
        :param market_id: Market id.
        :param int limit: (optional) Limit return size: 0-100, default: 100.
        :param bool mine: (optional) Include my orders, default False
        :param int start: (optional) Start to query for as timestamp, default: time()-(60*60*24).
        :param int stop:  (optional) Stop to query for as timestamp, default: time().
        :return: Dicts for trades:
            tradeid (str):            Trade id as integer string.
            tradeprice (float):       Price in market currency (eg. USD).
            initiate_ordertype (str): Type of order: Buy, Sell.
            datetime (str):           Time as datetime string.
            timestamp (int):          Time as timestamp.
            quantity (float):         Quantity in coin currency (eg. LTC).
            total (float):            Total in market currency (eg. USD).
        """
        return self._public_get(market_id, 'tradehistory',
                                limit=limit, mine=mine, start=start, stop=stop)

    def ohlc(self, market_id, start=None, stop=None, interval=None, limit=None):
        """List Open-high-low-close statements for the market - Unauthenticated.
        :param market_id:    Market id.
        :param int limit:    (optional) Limit return size: 0-100, default: 100.
        :param int start:    (optional) Start to query for as timestamp, default: time()-(60*60*24).
        :param int stop:     (optional) Stop to query for as timestamp, default: time().
        :param str interval: (optional) Interval as string: minute, hour, day, default: minute.
        :return: Dicts for Open-high-low-close statements:
            volume (float):  Traded volume in coin currency (eg. LTC).
            date (str):      Time as datetime string.
            timestamp (int): Time as timestamp.
            open (float):    Opening price in market currency (eg. USD).
            high (float):    Highest price in market currency (eg. USD).
            low (float):     Lowest price in market currency (eg. USD).
            close (float):   Closing price in market currency (eg. USD).
        """
        return self._public_get(market_id, 'ohlc',
                                start=start, stop=stop, interval=interval, limit=limit)
