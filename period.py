min1 = '1Min'
min5 = '5Min'
min15 = '15Min'
min30 = '30Min'
hour1 = '60min'
hour2 = '2hour'
hour4= '4hour'
day1 = '1day'

def get_ideal_period(symbol):
    if symbol == "btcusdt":
        return hour1
    if symbol == "ethusdt":
        return day1
    if symbol == "xrpusdt":
        return hour1