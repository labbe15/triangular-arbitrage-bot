import ccxt
import time

exchange = ccxt.bitget({
    'enableRateLimit': True
})

triangle = ['USDT', 'BTC', 'ETH']

def get_ticker(pair):
    try:
        ticker = exchange.fetch_ticker(pair)
        return {'bid': ticker['bid'], 'ask': ticker['ask']}
    except:
        return None

def check_arbitrage(start_amount=1000.0):
    a, b, c = triangle
    base = start_amount

    prices = {
        'BTC/USDT': get_ticker('BTC/USDT'),
        'ETH/BTC': get_ticker('ETH/BTC'),
        'ETH/USDT': get_ticker('ETH/USDT')
    }

    if None in prices.values():
        return "Erreur : Données manquantes"

    rate1 = 1 / prices['BTC/USDT']['ask']
    btc = base * rate1

    rate2 = 1 / prices['ETH/BTC']['ask']
    eth = btc * rate2

    rate3 = prices['ETH/USDT']['bid']
    usdt_final = eth * rate3

    profit = usdt_final - base
    roi = (usdt_final / base - 1) * 100

    print(f"USDT ➜ BTC ➜ E
