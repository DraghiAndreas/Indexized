import matplotlib.pyplot as plt
import random
import yfinance as yf



def tick_full(tick):
    d = {
    "VTI": "Vanguard Total Stock Market ETF",
    "SPY": "SPDR S&P 500 ETF Trust",
    "VOO": "Vanguard S&P 500 ETF",
    "SCHB": "Schwab U.S. Broad Market ETF",
    "DIA": "SPDR Dow Jones Industrial Average ETF Trust",
    "QQQ": "Invesco QQQ Trust (Nasdaq-100)",
    "XLK": "Technology Select Sector SPDR Fund",
    "XLF": "Financial Select Sector SPDR Fund",
    "XLE": "Energy Select Sector SPDR Fund",
    "XLY": "Consumer Discretionary Select Sector SPDR Fund",
    "XLI": "Industrial Select Sector SPDR Fund",
    "XLV": "Health Care Select Sector SPDR Fund",
    "XLC": "Communication Services Select Sector SPDR Fund",
    "XLU": "Utilities Select Sector SPDR Fund",
    "XLB": "Materials Select Sector SPDR Fund",
    "XLRE": "Real Estate Select Sector SPDR Fund",
    "VNQ": "Vanguard Real Estate ETF",
    "VXUS": "Vanguard Total International Stock ETF",
    "IXUS": "iShares Core MSCI Total International Stock ETF",
    "VEU": "Vanguard FTSE All-World ex-US ETF",
    "BND": "Vanguard Total Bond Market ETF",
    "AGG": "iShares Core U.S. Aggregate Bond ETF",
    "VIXY": "ProShares VIX Short-Term Futures ETF",
    "SH": "ProShares Short S&P500",
    "SQQQ": "ProShares UltraPro Short QQQ",
    "ARKK": "ARK Innovation ETF",
    "SOXX": "iShares Semiconductor ETF"
}
    return d[tick]

def hist(ticker,p):

    ticker = yf.Ticker(ticker)
    print(period_to_interval(p))
    pand = ticker.history(period=p,interval = period_to_interval(p))
    prices = pand['Close'].round(2).tolist()
    print(prices)
    start = prices[0]
    end = prices[-1]
    change = round(end - start, 2)
    percent = round((change / start) * 100, 2)
    return start,end,change,percent,prices

#def price_return(t):
#    return yf.Ticker(t).info['regularMarketPrice']

def graph_color(p):
    return '#d60a22' if p<0 else '#056354'

def map_change(change):
    
    if change >= 0:
        change = min(change, 15)
        if change <= 1:
            start, end = (156,204,153), (126,204,123)
            frac = (change / 1)
        elif change <= 5:
            start, end = (126,204,123), (106,190,103)
            frac = (change - 1) / (5 - 1)
        elif change <= 15:
            start, end = (106,190,103), (80,160,80)
            frac = (change - 5) / (15 - 5)
        else:
            return (80/255,160/255,80/255)
    else:    
        change = max(change, -15)
        if change >= -0.5:
            start, end = (205,115,117), (225,95,97)
            frac = (abs(change) / 0.5)
        elif change >= -3:
            start, end = (225,95,97), (255,45,47)
            frac = (abs(change) - 0.5) / (3 - 0.5)
        elif change >= -15:
            start, end = (255,45,47), (140,0,0)
            frac = (abs(change) - 3) / (15 - 3)
        else:
            return (130/255,0,0)

    r = float(start[0] + frac * (end[0] - start[0]))
    g = float(start[1] + frac * (end[1] - start[1]))
    b = float(start[2] + frac * (end[2] - start[2]))

    return (r/255,g/255,b/255)

    

def period_to_interval(period):
    periods = ['1d','5d','1mo','6mo','ytd','1y','5y','max']
    intervals = ['1m','15m','1d','1d','1d','1d','1wk','1mo']
    for i in range(len(periods)):
        if period == periods[i]:
            return intervals[i]
    return 'Invalid'


def num_to_month(num):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if 1 <= num <= 12:
        return months[num - 1]
    return 'Invalid'


def date_selector(dates,period):
        idx = dates.index
        if period == '1d':
             return [ts.strftime("%H") if ts.minute == 0 else '' for ts in idx]
        elif period == '5d':
             return [ts.strftime(r"%m/%d") if ts.hour == 9 and ts.minute == 30 else '' for ts in idx]
        elif period in ['1mo','6mo','ytd','1y']:
            previous_month = -1
            l = []
            for ts in idx:
                if ts.month != previous_month and ts.day < 15:
                    month = num_to_month(ts.month)
                    if month == 'Jan':
                        month += f'\n{ts.year}'
                    l.append(month)
                    previous_month = ts.month
                else:
                    l.append('')
            return l
        elif period == '5y':
            previous = -1
            l=[]
            for ts in idx:
                if ts.year != previous and ts.month < 6:
                    l.append(ts.year)
                    previous=ts.year
                else:
                    l.append('')
            return l
        elif period == 'max':
            previous = -1
            l = []
            for ts in idx:
                if ts.year != previous and ts.year%5==0:
                    l.append(ts.year)
                    previous = ts.year
                else:
                    l.append('')
            return l

def random_quote():
    l = ['It is hard to fail, but it is worse never to have tried to succeed.',
         'When you\'re at the end of your rope, tie a knot and hold on.',
         'The only man who never makes mistakes is the man who never does anything.',
         'Knowing what\'s right doesn\'t mean much unless you do what\'s right.',
         'Keep your eyes on the stars and your feet on the ground.',
         'If you could kick the person in the pants responsible for most of your trouble,\n you wouldn\'t sit for a month.',
         'In any moment of decision, the best thing you can do is the right thing. \nThe worst thing you can do is nothing.',
         'Courage is not having the strength to go on; it is going on when you don\'t have the strength.',
         'Never throughout history has a man who lived a life of ease left a name worth remembering.',
         'The reason fat men are good natured is they can neigher fight nor run.',
         'I put myself in the way of things happening, and they happened'
         ]
    return random.choice(l)