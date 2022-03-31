import ccxt
import os
from binance.client import Client
from detect import determine
from config import *
from setup import setup, leverage

# print(ccxt.exchanges)

exchange = ccxt.binance()
markets = exchange.load_markets()


exchange_id = 'binance'


def long():
    pass
    # exchange.futures_create_order(
    #     symbol='BTCUSDT', side='BUY', type='MARKET', quantity=trade_quantity)


def short():
    pass


def algorithm(x_max_before, indicator_before, image):
    indicator_after, x_max_after = determine(image)
    if ((indicator_before == "NULL") and (x_max_before == 0)):  # program just started
        if (indicator_after == "BUY"):
            # buy
            print("BUY!")
            pass
        else:
            # sell
            print("SELL!")
            pass
    elif (indicator_before != indicator_after):  # change from sell to buy or vice versa
        # close position of indicator_before
        # open position of indicator_after
        pass
    elif (abs(x_max_after - x_max_before) >= 10):  # signal lost
        # close position
        pass
