import ccxt
import os
import sys
from binance.client import Client
from config import *

print('CCXT Version:', ccxt.__version__)


def leverage():

    exchange = ccxt.binance({
        'apiKey': 'cmicC5GYmYOG3ksSbOjZcjKanqnhQbIic0aaBSOx6Qjn0DAnUzB0kotSwxDbNs9t',
        'secret': 'fA9hSDXwLsRk0SNcx8OqAUhULHLbgrjbIRbGhIYaYPgowp5r1svxJUZuGaFqFtRF',
        'enableRateLimit': True,
        'options': {
            'defaultType': 'future',
        }
    })

    exchange.load_markets()

    symbol = 'BTC/USDT'
    market = exchange.market(symbol)
    leverage = 5

    response = exchange.fapiPrivate_post_leverage({
        'symbol': market['id'],
        'leverage': leverage,
        'marginType': 'ISOLATED',
    })
    balance = exchange.fetch_balance()
    positions = balance['info']['positions'][112]
    print(positions)


def user_balance():
    client = Client(api_key, api_secret)

    price_dict = client.futures_mark_price(symbol='BTCUSDT')
    btc_price = float(price_dict['markPrice'])

    USDT_dict = client.futures_account_balance()
    user_balance = USDT_dict[1]['balance']
    return user_balance


def btc_price():
    client = Client(api_key, api_secret)
    price_dict = client.futures_mark_price(symbol='BTCUSDT')
    btc_price = float(price_dict['markPrice'])
    return btc_price

# trade_size = 10
# trade_quantity = (trade_size)/(btc_price)        # amount of btc


# user_balance()
# btc_price()
leverage()
