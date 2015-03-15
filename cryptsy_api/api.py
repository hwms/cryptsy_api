# -*- coding: utf-8 -*-
from . import base, old_public, chart, old_private, markets, currencies, order, trigger, converter

__all__ = ['CryptsyApi']

class CryptsyApi(base.Api):
    def __init__(self, config=None, session=None):
        super(CryptsyApi, self).__init__(config, session)
        kwargs = {'config': self.config, 'session': self.session}
        self.markets = markets.MarketsApi(**kwargs)
        self.currencies = currencies.CurrenciesApi(**kwargs)
        self.order = order.OrderApi(**kwargs)
        self.trigger = trigger.TriggerApi(**kwargs)
        self.converter = converter.ConverterApi(**kwargs)

        self.old_public = old_public.OldPublicApi(**kwargs)
        self.old_private = old_private.OldPrivateApi(**kwargs)
        self.chart = chart.ChartApi(**kwargs)

    def info(self):
        """Account informations - Authenticated.
        :return: Dict of account informations:
            id (str):          User id as integer.
            username (str):    Username.
            accounttype (str): Account type: Personal/?.
            email (str):       Email.
            first_name (str):  First name.
            last_name (str):   Last name.
            trade_key (str):   Trade key as 40 char hex.
        """
        return self.query('info')

    def balances(self, currency_id=None, balance_type=None):
        """List balances for currency/ies - Authenticated.
        :param currency_id:      (optional) Currency id.
        :param str balance_type: (optional) Balance type: available, held, all, default: all.
        :return: Dict of dicts per balance type for currency/ies:
            {'held': {id:balance,..}, 'available': {id:balance,..}}
            held (dict):      Held balances for open order.
            available (dict): Available balances for trade.
                id (str):        Currency id as integer.
                balance (float): Balance in coin currency (eg. LTC).

        Note: in Beta 'held' can contain an empty list, 'available' seems to always contain a dict.
        """
        return self.query('balances', currency_id, type=balance_type)

    def deposits(self, currency_id=None, limit=None):
        """List all deposits and withdrawals for currencies/y - Authenticated.
        :param currency_id: (optional) Currency id.
        :param int limit:   (optional) Limit return size: 0-100, default: 100.
        :return: Dict(s) for currency/ies:
            trxid (str):     Network transaction id (if available).
            amount (str):    Amount in coin currency (eg. LTC) as float.
            address (str):   Address of sender/receiver.
            currency (str):  Currency id as integer string.
            fee (float):     Fee paid for the transaction.
            status (str):    Status: confirmed/?.
            datetime (str):  Transaction time of the deposit as datetime.
            timezone (str):  Transaction time timezone code, eg. EST.
            timestamp (int): Transaction time as timestamp.
        """
        return self.query('deposits', currency_id, limit=limit)

    def addresses(self, currency_id=None, trade_key=None):
        """List addresses for all currencies/a currency - Authenticated.
        :param currency_id:   (optional) Currency id.
        :param str trade_key: (optional) Valid trade key.
        :return: Dict with address per currency id:
            id (str):        Currency id as integer string.
            address (float): Address.
        """
        return self.query('addresses', currency_id, tradekey=trade_key)

    def orders(self, market_id, order_type=None):
        """List open orders (for the market?) - Authenticated.
        :param market_id:      Market id.
        :param str order_type: (optional) Order type: buy, sell, both, default: both.
        :return: Dict with order dicts (sellorders and/or buyorders depending on order_type):
            orderid (str):         Order id as integer string.
            ordertype (str):       Order type: Buy/Sell.
            marketid (str):        Market id as integer string.
            orig_quantity (float): Original quantity in coin currency (eg. LTC).
            quantity (float):      Quantity in coin currency (eg. LTC).
            total (float):         Total in market currency (eg. USD).
            price (float):         Price in coin currency (eg. LTC).
            created (str):         Creation time as datetime string.
            timestamp (str):       Creation time as timestamp.

        Note: market_id seems to has no effect in Beta.
        """
        return self.query('orders', market_id, type=order_type)

    def triggers(self, market_id, order_type=None):
        """List your own triggers active (for the market) - Authenticated.
        :param market_id:      Market id.
        :param str order_type: (optional) Order type: buy, sell, both, default: both.
        :return: Dict(s) for (a) market(s).
            triggerid (str):          Trigger id as integer string.
            action (str):             Order type: Buy/Sell.
            comparison (str):         Comparison sign (<= or =>), eg. for "When coin price <=".
            trigger_price (float):    Coin price to trigger in market currency (eg. USD).
            trigger_quantity (float): Maximum quantity to trade in coin currency (eg. LTC).
            orderprice (float):       Order price to make in market currency (eg. USD).
            expires (str):            Expire time as datetime string.
            expires_timestamp (int):  Expire time as timestamp.

        Note: marketid/triggerid? and type don't work and market ids in the result are missing imo.
        """
        return self.query('triggers', market_id, type=order_type)

    def tradehistory(self, limit=None, start=None, stop=None):
        """List own tradehistory - Authenticated.
        :param int limit: (optional) Limit return size: 0-100, default: 100.
        :param int start: (optional) Start to query for as timestamp, default: time()-(60*60*24).
        :param int stop:  (optional) Stop to query for as timestamp, default: time().
        :return: Dicts for trades:
            marketid (str):           Market id as integer string.
            orderid (str):            Order id as integer string.
            tradeid (str):            Trade id as integer string.
            tradetype (str):          Trade type: Buy/Sell.
            initiate_ordertype (str): Order type: Buy/Sell.
            quantity (float):         Quantity in coin currency (eg. LTC).
            tradeprice (float):       Price in market currency (eg. USD).
            fee (float):              Included fee in market currency (eg. USD).
            total (float):            Total in market currency (eg. USD).
            datetime (str):           Time as datetime string.
            timestamp (int):          Time as timestamp.
        """
        return self.query('tradehistory', limit=limit, start=start, stop=stop)

    def validatetradekey(self, trade_key):
        """Validate a trade key - Authenticated.
        :param str trade_key: Trade key as 40 char hex.
        :return: List with one string: 'Tradekey is valid.' or 'Tradekey is invalid.'.
            Also the success indicator returns either True or False.
        """
        return self.query('validatetradekey', tradekey=trade_key)

    def transfers(self, market_id=None, transfer_type=None, limit=None):
        """List transfers for (a) market(s) - Authenticated.
        :param market_id:          (optional) Market id.
        :param str transfer_type:  (optional) in, out, both.
        :param int limit:          (optional) Limit return size: 0-100, default: 100.
        :return: Dict with transfer dicts for 'in' and 'out': ?

        Note: never done this, examples needed.
        """
        return self.query('transfers', market_id, type=transfer_type, limit=limit)

    def withdrawals(self, currency_id, limit=None):
        """List withdrawas for all currencies/a currency - Authenticated.
        :param currency_id: (optional) Currency id.
        :param int limit:   (optional) Limit return size: 0-100, default: 100.
        :return: Dicts for withdrawals for all currencies/a currency:
            trxid (str):      Network transaction id (if available).
            amount (str):     Amount in coin currency (eg. LTC) as float.
            currencyid (str): Currency id as integer string.
            fee (float):      Included fee in coin currency (eg. LTC) as float.
            address (str):    Address of receiver.
            status (str):     Status: confirmed/?. Note: missing in Beta.
            datetime (str):   Transaction time as datetime.
            timezone (str):   Transaction time timezone code, eg. EST.
            timestamp (int):  Transaction time as timestamp.
        """
        return self.query('withdrawals', currency_id, limit=limit)

    def transfer(self, currency_id, notificationtoken, tradekey, quantity):
        """Inititate a transfer - Authenticated.
        :param currency_id:           Currency id.
        :param str notificationtoken: Token posted to notification url (with address and amount).
        :param str trade_key:         Trade key to transfer to as 40 char hex.
        :param float quantity:        Quantity in coin currency to transfer.
        :return: ?
        Note: never done this, examples needed.
        """
        return self.query('transfer', currency_id, notificationtoken=notificationtoken,
                          tradekey=tradekey, quantity=quantity)

    def withdraw(self, currency_id, notificationtoken, address, quantity):
        """Inititate a withdrawal - Authenticated.
        :param currency_id:           Currency id.
        :param str notificationtoken: Token posted to notification url (with address and amount).
        :param str address:           Address to transfer to.
        :param float quantity:        Quantity in coin currency to transfer.
        :return: ?
        Note: never done this by api, examples needed.
        """
        return self.query('withdraw', currency_id, notificationtoken=notificationtoken,
                          address=address, quantity=quantity)
