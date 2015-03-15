# -*- coding: utf-8 -*-
from . import base

class OldPrivateApi(base.Api):

    def _request(self, *args, **kwargs):
        kwargs = dict(dict(url=self.config.old_private_url), **kwargs)
        return super()._request(*args, **kwargs)

    def _post(self, method, marketid=None, **params):
        return super()._post(method=method, marketid=marketid, **params)

    def info(self):
        """User and Server informations - Authenticated.
        :return: Dict of balance and server informations:
            balances_available (dict):     Available amounts per code as float string.
            balances_available_btc (dict): Available amount in BTC per code as float string.
            balances_hold (dict):          On hold amount per code as float string.
            balances_hold_btc (dict):      On hold amount in BTC per code as float string.
            openordercount (int):          Count of open orders.
            serverdatetime (str):          Server time as datetime.
            servertimezone (str):          Server time timezone code, eg. EST.
            servertimestamp (str):         Server time as timestamp.
        """
        return self._post('getinfo')
    getinfo = info

    def markets(self):
        """Market informations for all active markets - Authenticated.
        :return: Dicts for markets:
            marketid (str):                Market id as int.
            label (str):                   Name, eg. LTC/USD.
            created (str):                 Creation time as datetime (EST).
            primary_currency_code (str):   Coin currency code, eg: LTC.
            primary_currency_name (str):   Coin currency name, eg: LiteCoin.
            secondary_currency_code (str): Market currency code, eg: USD.
            secondary_currency_name (str): Market currency name, eg: US Dollar.
            last_trade (str):              Last trade price in market currency (eg. USD) as float.
            high_trade (str):              24h highest price in market currency (eg. USD) as float.
            low_trade (str):               24h lowest price in market currency (eg. USD) as float.
            current_volume (str):          24h volume in coin currency (eg. LTC) as float.
            current_volume_btc (str):      24h volume in BTC as float.
            current_volume_usd (str):      24h volume in USD as float.
        """
        return self._post('getmarkets')
    getmarkets = markets

    def currencies(self):
        """Currency informations for all currencies - Authenticated.
        :return: Dicts for currencies:
            currencyid (str):      Currency id as int.
            code (str):            Code, eg. LTC.
            name (str):            Name, eg. LiteCoin.
            maintenancemode (str): Currency maintence mode as int (0:No issues, 1:Maintenance,
                                   2:Updating wallet, 3:Network issues).
            withdrawalfee (str):   Withdrawal fee in percent as float.
        """
        return self._post('getcoindata')
    getcoindata = currencies

    def wallets(self):
        """Status information for wallets - NDA required.
        :return: Dicts of wallet statuses:
            currencyid (str):      Currency id as int.
            code (str):            Code, eg. LTC.
            name (str):            Name, eg. LiteCoin.
            blockcount (str):      Blockcount from last update as int.
            difficulty (str):      Difficulty from last update as int.
            version (str):         Version as of last update.
            peercount (str):       Connected peers from last update as int.
            hashrate (str):        Network hashrate from last update as float.
            gitrepo (str):         Git repository url.
            withdrawalfee (str):   Withdrawal fee in percent as float.
            lastupdate (str):      Last update as datetime (EST).
            maintenancemode (str): Maintence mode as int (0:No issues, 1:Maintenance,
                                   2:Updating wallet, 3:Network issues).
        """
        return self._post('getwalletstatus')
    getwalletstatus = wallets

    def transactions(self):
        """Transaction information for all deposits and withdrawals - Authenticated.
        :return: Dicts of transactions:
            trxid (str):     Network transaction id (if available).
            currency (str):  Currency code, eg. LTC.
            address (str):   Address of sender/receiver.
            type (str):      Transaction type: Deposit/Withdrawal.
            amount (str):    Amount in coin currency (eg. LTC) as float.
            fee (float):     Included fee in coin currency (eg. LTC) as float.
            datetime (str):  Transaction time as datetime.
            timezone (str):  Transaction time timezone code, eg. EST.
            timestamp (int): Transaction time as timestamp.
        Note: status is missing.
        """
        return self._post('mytransactions')
    mytransactions = transactions

    def markettrades(self, marketid):
        """
        :param marketid: Market id for which you are querying
        :return: Dicts of last 1000 trades for this market, in date descending order.
            tradeid                 - A unique id for the trade
            datetime                - Server datetime trade occurred
            tradeprice              - Price the trade occurred at
            quantity                - Quantity traded
            total                   - Total value of trade (tradeprice * quantity)
            initiate_ordertype      - Type of order which initiated this trade
        """
        return self._post('markettrades', marketid)

    def marketorders(self, marketid):
        """
        :param marketid: Market id for which you are querying
        :return: Two dicts, first for sellorders (price asc) and second for buyorders (price desc).
            sellprice               - If a sell order, price which order is selling at
            buyprice                - If a buy order, price the order is buying at
            quantity                - Quantity on order
            total                   - Total value of order (price * quantity)
        """
        return self._post('marketorders', marketid)

    def mytrades(self, marketid=None, limit=200):
        """
        :param marketid: Market id for which you are querying
        :param limit: (optional) Limit the number of results. Default: 200
        :return: Dicts of trades for this market, in date descending order.
            tradeid                 - An integer identifier for this trade
            tradetype               - Type of trade (Buy/Sell)
            datetime                - Server datetime trade occurred
            tradeprice              - The price the trade occurred at
            quantity                - Quantity traded
            total                   - Total value of trade (tradeprice * quantity) - Without fees
            fee                     - Fee Charged for this Trade
            initiate_ordertype      - Type of order which initiated this trade
            order_id                - Original order id this trade was executed against
        """
        return self._post('mytrades', marketid, limit=limit)

    def allmytrades(self, startdate=None, enddate=None):
        """
        :param startdate: (optional) Starting date for query (format: yyyy-mm-dd)
        :param enddate: (optional) Ending date for query (format: yyyy-mm-dd)
        :return: Dicts of trades for this market, in date descending order.
            tradeid                 - An integer identifier for this trade
            tradetype               - Type of trade (Buy/Sell)
            datetime                - Server datetime trade occurred
            marketid                - Market id in which the trade occurred
            tradeprice              - Price the trade occurred at
            quantity                - Quantity traded
            total                   - Total value of trade (tradeprice * quantity) - Without fees
            fee                     - Fee Charged for this Trade
            initiate_ordertype      - The type of order which initiated this trade
            order_id                - Original order id this trade was executed against
        """
        return self._post('allmytrades', startdate=startdate, enddate=enddate)

    def myorders(self, marketid):
        """
        :param marketid: Market id for which you are querying
        :return: Dicts of your orders for this market listing your current open sell and buy orders.
            orderid                 - Order id for this order
            created                 - Datetime the order was created
            ordertype               - Type of order (Buy/Sell)
            price                   - Price per unit for this order
            quantity                - Quantity remaining for this order
            total                   - Total value of order (price * quantity)
            orig_quantity           - Original Total Order Quantity
        """
        return self._post('myorders', marketid)

    def depth(self, marketid):
        """
        :param marketid: Market id for which you are querying
        :return: Dict with 'sell' and 'buy' lists representing the market depth.
            Format: {'sell': [[price, quantity], [price, quantity], ..],
                     'buy': [[price, quantity], [price, quantity], ..]}
        """
        return self._post('depth', marketid)

    def allmyorders(self):
        """List of all order infos.
        :return: Dicts of all open orders for your account.
            orderid                 - Order id for this order
            marketid                - Market id this order was created for
            created                 - Datetime the order was created
            ordertype               - Type of order (Buy/Sell)
            price                   - The price per unit for this order
            quantity                - Quantity remaining for this order
            total                   - Total value of order (price * quantity)
            orig_quantity           - Original Total Order Quantity
        """
        return self._post('allmyorders')

    def createorder(self, marketid, ordertype, quantity, price):
        """Create an order.
        :param market_id:         Market id.
        :param quantity (float):  Quantity to order in coin currency, eg. LTC.
        :param order_type (str):  Type of order: buy/sell.
        :param price (float):     Price per coin unit in market currency, eg. USD.
        :return: A dict containing the orderid of the created order.
            orderid                 - If successful, the Order id for the order which was created
            moreinfo                - HTML info about the order creation
        """
        return self._post('createorder', marketid,
                          ordertype=ordertype, quantity=quantity, price=price)

    def create_sellorder(self, marketid, quantity, price):
        """
        :param marketid: Market id for which you are creating an order for
        :param quantity: Amount of units you are selling in this order
        :param price: Price per unit you are selling at
        :return: A dict containing the orderid of the created order.
            orderid                 - If successful, the Order id for the order which was created
            moreinfo                - HTML info about the order creation
        """
        return self.createorder(marketid, 'sell', quantity, price)

    def create_buyorder(self, marketid, quantity, price):
        """
        :param marketid: Market id for which you are creating an order for
        :param quantity: Amount of units you are buying in this order
        :param price: Price per unit you are buying at
        :return: A dict containing the orderid of the created order.
            orderid                 - If successful, the Order id for the order which was created
            moreinfo                - HTML info about the order creation
        """
        return self.createorder(marketid, 'buy', quantity, price)

    def cancelorder(self, orderid):
        """ Cancel a specific order.
        :param orderid: Order id for which you would like to cancel
        :return: If successful, it will return a success code.
        """
        return self._post('cancelorder', orderid=orderid)

    def cancelmarketorders(self, marketid):
        """
        :param marketid: Market id for which you would like to cancel all open orders
        :return: Dicts with return information on each order cancelled.
        """
        return self._post('cancelmarketorders', marketid)

    def cancelallorders(self):
        """
        :return: Dicts with return information on each order cancelled.
        """
        return self._post('cancelallorders')

    def calculatefees(self, marketid, ordertype, quantity, price):
        """
        :param marketid: Market id of which market you're calculating fees for
        :param ordertype: Order type you are calculating for (Buy/Sell)
        :param quantity: Amount of units you are buying/selling
        :param price: Price per unit you are buying/selling at
        :return: A dict containing the fee and net total.
            fee                     - Fee that would be charged for provided inputs
            net                     - Net total with fees
            discount                - Discount percentage included
        """
        return self._post('calculatefees', marketid,
                          ordertype=ordertype, quantity=quantity, price=price)

    def calculate_sellfees(self, marketid, quantity, price):
        """
        :param marketid: Market id of which market you're calculating fees for
        :param quantity: Amount of units you are selling
        :param price: Price per unit you are selling at
        :return: A dict containing the fee and net total.
            fee                     - Fee that would be charged for provided inputs
            net                     - Net total with fees
            discount                - Discount percentage included
        """
        return self.calculatefees(marketid, 'Sell', quantity, price)

    def calculate_buyfees(self, marketid, quantity, price):
        """
        :param marketid: Market id of which market you're calculating fees for
        :param quantity: Amount of units you are buying
        :param price: Price per unit you are buying at
        :return: A dict containing the fee and net total.
            fee                     - Fee that would be charged for provided inputs
            net                     - Net total with fees
            discount                - Discount percentage included
        """
        return self.calculatefees(marketid, 'Buy', quantity, price)

    def generatenewaddress(self, currencyid=None, currencycode=None):
        """
        (either currencyid OR currencycode required - you do not have to supply both)
        :param currencyid: Currency ID for the coin you want to generate a new address for
        :param currencycode: Currency Code for the coin you want to generate a new address for
        :throws ValueError: Fails if neither of the parameters are given.
        :return: A dict containing the new address.
            address                 - The new generated address
        """
        return self._post('generatenewaddress',
                          currencyid=currencyid, currencycode=currencycode)

    def mytransfers(self):
        """
        :return: Dicts of all transfers of your account sorted by requested datetime descending.
            currency                - Currency being transfered
            request_timestamp       - Datetime the transfer was requested/initiated
            processed               - Indicator if transfer has been processed (1) or not (0)
            processed_timestamp     - Datetime of processed transfer
            from                    - Username sending transfer
            to                      - Username receiving transfer
            quantity                - Quantity being transfered
            direction               - Indicates if transfer is incoming or outgoing (in/out)
        """
        return self._post('mytransfers')

    def makewithdrawal(self, address, amount):
        """
        :param address: Pre-approved Address for which you are withdrawing to (see settings page).
        :param amount: Amount you are withdrawing. Supports up to 8 decimal places.
        :return: Either successful or error. If error, gives reason for error.
        """
        return self._post('makewithdrawal', address=address, amount=amount)

    def getmydepositaddresses(self):
        """
        :return: Dict of all deposit addresses {code: address, ..}.
        """
        return self._post('getmydepositaddresses')

    def getorderstatus(self, orderid):
        """
        :param orderid: Order id for which you are querying
        :return: tradeinfo is a list of all the trades that have occured in your order.
            Where orderinfo shows realtime status of the order.
            Orderinfo contains the 'active'; a boolean object showing if the order is still open.
            Orderinfo also contains 'remainqty' which shows the quantity left in your order.
            tradeinfo               - A list of all trades that have occuried in your order.
            orderinfo               - Information regarding status of the order.
                active              - True if the order is active.
                remainqty           - Quantity remaining.
        """
        return self._post('getorderstatus', orderid=orderid)
