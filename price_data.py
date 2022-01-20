import requests

base_url = 'https://api-aws.huobi.pro'
binance_price_base_url = 'https://api.binance.com/api/v3/klines?'
order_book_base_url = 'https://api.huobi.pro/market/'

order_book_depth = 'depth?='
order_book_symbol = '&symbol='
order_book_step = '&type='

currencies_base_url = '/market/history/'
currencies_time = 'kline?period='
currencies_data_amount = '&size='
currencies_symbol = '&symbol='

binance_price_symbol = 'symbol='
binance_price_interval = '&interval='
binance_price_limit = '&limit='



def get_huobi_price_data(symbol, time_period, data_amount):

    currencies_url = base_url + currencies_base_url + currencies_time + str(time_period).lower() + currencies_data_amount + str(
        data_amount) + currencies_symbol + symbol
    resp = requests.get(currencies_url)
    resp_json = resp.json()
    if 'data' in resp_json:
        data_list = resp_json['data']
        return data_list
    else: return None

def get_binance_price_data(symbol, time_period, data_amount):
    price_url = binance_price_base_url + binance_price_symbol + symbol + binance_price_interval + str(time_period) + binance_price_limit + str(data_amount)
    resp = requests.get(price_url)
    resp_json = resp.json()
    return resp_json

def get_order_book_data(symbol, depth, step, type):
    order_book_url = order_book_base_url + order_book_depth + str(depth) + order_book_symbol + symbol + order_book_step + step
    resp = requests.get(order_book_url)
    resp_json = resp.json()
    if type == 'bids':
        data_list  = resp_json['tick']['bids']
        return data_list
    elif type == 'asks':
        data_list = resp_json['tick']['asks']
        return data_list
    elif type == 'all':
        data_list_bids = resp_json['tick']['bids']
        data_list_asks = resp_json['tick']['asks']
        return data_list_bids, data_list_asks