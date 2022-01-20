import datetime
import time

# from config import *
import requests

import config
import ema
import risk_calculator
import strat_test
import strategy_c

import symbols
import period
import price_data
import sma
import macd
import rsi
import data_file

# /market/history/kline?period=60min&size=1&symbol=btcusdt
base_url = 'https://api-aws.huobi.pro'
currencies_base_url = '/market/history/'
currencies_time = 'kline?period='
currencies_data_amount = '&size='
currencies_symbol = '&symbol='
# strat_test.calculate_strat()
print('---Start---')
print('A5')

current_amount = []
h = []
full = 0



def buy_coin(amount, other_price):
    new_amount = amount * other_price
    #current_amount.clear()
    #h.append(new_amount)
    #current_amount.append(new_amount)
    return new_amount


def sell_coin(amount, other_price):
    new_amount = amount / other_price
    #current_amount.clear()
    #h.append(new_amount)
    #current_amount.append(new_amount)
    return new_amount


while True:
    start_money = 100
    start_amount = 1
    fee = 0.3

    for a in symbols.get_main_syms():
        current_amount.clear()
        current_amount.append(start_amount)
        h.append(1)
        for b in symbols.get_main_syms():
            if a != b:

                first = price_data.get_huobi_price_data(b + a, period.min1, 1)

                if first is None:
                    first = price_data.get_huobi_price_data(a + b, period.min1, 1)
                    new_amount1 = buy_coin(current_amount[0], first[0]['close'])

                else:
                    new_amount1 = sell_coin(current_amount[0], first[0]['close'])

                for c in symbols.get_all_single_symbols():
                    if a != b and b != c and a != c:

                        second = price_data.get_huobi_price_data(c + b, period.min1, 1)

                        if second is None:
                            second = price_data.get_huobi_price_data(b + c, period.min1, 1)
                            if second is None: continue
                            new_amount2 = buy_coin(new_amount1, second[0]['close'])

                        else:
                            new_amount2 = sell_coin(new_amount1, second[0]['close'])

                        if c != a:

                            third = price_data.get_huobi_price_data(c + a, period.min1, 1)
                            if third is None:
                                third = price_data.get_huobi_price_data(a + c, period.min1, 1)
                                if third is None: continue
                                new_amount3 = sell_coin(new_amount2, third[0]['close'])

                            else:
                                new_amount3 = buy_coin(new_amount2, third[0]['close'])


                            perce = (new_amount3/start_amount)*100
                            if perce > 100.3:
                                full += (perce - 100) - fee
                                current_profit = (perce-100)-fee
                                print(f'profit: {format(current_profit, "f")}% full: {full}% route: {a} -> {b} -> {c} -> {a}')

                            #else: print(f'start amount: {start_amount} -> end amount: {format(new_amount3, "f")} route: {a} -> {b} -> {c} -> {a}')
