# -*- coding: utf-8 -*-
from . import base

class CurrenciesApi(base.Api):
    _path = 'currencies',

    def __call__(self, currency_id=None):
        """List currency info for currencies/y - Unauthenticated.
        :param currency_id: (optional) Currency id.
        :return: Dict(s) for currencies/y:
            id (str):          Currency id as integer.
            code (str):        Code, eg. LTC.
            name (str):        Name, eg. LiteCoin.
            maintenance (str): Maintence mode as integer (0 - No issues, 1 - Maintenance,
                               2 - Updating wallet, 3 - Network issues).
        """
        return self._public_get(currency_id)

    def markets(self, currency_id):
        """List markets info for currency - Unauthenticated.
        :param currency_id: Currency id.
        :return: Dict for the currency with market dicts:
            id (str):          Currency id as integer.
            code (str):        Code, eg. LTC.
            name (str):        Name, eg. LiteCoin.
            markets (dicts):   Market infos where the currency is coin currency.
                id (str):                 Market id as integer.
                label (str):              Label, eg. LTC/USD.
                coin_currency_id (str):   Coin currency as integer, eg: 2.
                market_currency_id (str): Market currency as integer, eg: 1.
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
        return self._public_get(currency_id, 'markets')

    def status(self, currency_id):
        """Status info for currency - NDA required.
        :param currency_id: Currency id.
        :return: Dict for currency status:
            id (str):              Currency id as integer string.
            code (str):            Code, eg. LTC.
            name (str):            Name, eg. LiteCoin.
            blockcount (str):      Blockcount as integer string from last update.
            difficulty (str):      Difficulty as integer string from last update.
            version (str):         Version as of last update.
            peercount (str):       Connected peers as integer string from last update.
            hashrate (str):        Network hashrate from last update.
            gitrepo (str):         Git repository url.
            withdrawalfee (str):   Fee charged for withdrawals as float string.
            lastupdate (str):      Last update time as datetime (EST) string.
            maintenancemode (str): Maintence mode as integer string (0 - No issues,
                                   1 - Maintenance, 2 - Updating wallet, 3 - Network issues).
        """
        return self._public_get(currency_id, 'status')
