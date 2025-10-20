import yfinance as yf
from . basic import *
from . portfolio import *
from pyfiglet import Figlet
from colorama import init, Fore, Style
from datetime import datetime
from . cache_test import cache
from random import uniform
from tabulate import tabulate
from math import pow
import sqlite3
import os
init()

tickers = [
    "VTI", "SPY", "VOO", "SCHB", "VXUS", "IXUS", "VEU", "BND", "AGG", "XLK", "VNQ",
    "DIA", "QQQ",
    "XLF", "XLE", "XLY", "XLI", "XLV", "XLC", "XLU", "XLB", "XLRE",
    "VIXY", "SH", "SQQQ",
    "ARKK", "SOXX"
]


from tabulate import tabulate

def all_funds():
    best_us = [
        ["VTI", "Vanguard Total Stock Market ETF"],
        ["SPY", "SPDR S&P 500 ETF Trust"],
        ["VOO", "Vanguard S&P 500 ETF"],
        ["SCHB", "Schwab U.S. Broad Market ETF"],
        ["DIA", "SPDR Dow Jones Industrial Average ETF Trust"],
        ["QQQ", "Invesco QQQ Trust (Nasdaq-100)"]
    ]

    sectors = [
        ["XLK", "Technology Select Sector SPDR Fund"],
        ["XLF", "Financial Select Sector SPDR Fund"],
        ["XLE", "Energy Select Sector SPDR Fund"],
        ["XLY", "Consumer Discretionary Select Sector SPDR Fund"],
        ["XLI", "Industrial Select Sector SPDR Fund"],
        ["XLV", "Health Care Select Sector SPDR Fund"],
        ["XLC", "Communication Services Select Sector SPDR Fund"],
        ["XLU", "Utilities Select Sector SPDR Fund"],
        ["XLB", "Materials Select Sector SPDR Fund"],
        ["XLRE", "Real Estate Select Sector SPDR Fund"],
        ["VNQ", "Vanguard Real Estate ETF"]
    ]

    international = [
        ["VXUS", "Vanguard Total International Stock ETF"],
        ["IXUS", "iShares Core MSCI Total International Stock ETF"],
        ["VEU", "Vanguard FTSE All-World ex-US ETF"]
    ]

    bonds = [
        ["BND", "Vanguard Total Bond Market ETF"],
        ["AGG", "iShares Core U.S. Aggregate Bond ETF"]
    ]

    volatility_inverse = [
        ["VIXY", "ProShares VIX Short-Term Futures ETF"],
        ["SH", "ProShares Short S&P500"],
        ["SQQQ", "ProShares UltraPro Short QQQ"]
    ]

    thematic = [
        ["ARKK", "ARK Innovation ETF"],
        ["SOXX", "iShares Semiconductor ETF"]
    ]

    print('\nBest U.S. Broad Market ETFs\n')
    print(tabulate(best_us, headers=["Ticker", "Name"], tablefmt="fancy_grid"))

    print("\nSector ETFs\n")
    print(tabulate(sectors, headers=["Ticker", "Name"], tablefmt="fancy_grid"))

    print("\nBest International ETFs\n")
    print(tabulate(international, headers=["Ticker", "Name"], tablefmt="fancy_grid"))

    print("\nBond ETFs\n")
    print(tabulate(bonds, headers=["Ticker", "Name"], tablefmt="fancy_grid"))

    print("\nVolatility & Inverse ETFs\n")
    print(tabulate(volatility_inverse, headers=["Ticker", "Name"], tablefmt="fancy_grid"))

    print("\nThematic ETFs\n")
    print(tabulate(thematic, headers=["Ticker", "Name"], tablefmt="fancy_grid"))


def validate():
    while True:
        try:
            ticker = input("Enter TICKER : \n")
            if ticker.upper() in tickers:
                return ticker
            else:
                raise ValueError
        except ValueError:
            print('-INVALID TICKER-')
            pass

def date_test(ticker):
    ticker = yf.Ticker(ticker)
    p = '6mo'
    day = ticker.history(p,interval = period_to_interval(p))
    print(day)
    dates = date_selector(day,p)
    print(dates)

def general_info(tickname):
    ticker = yf.Ticker(tickname)
    data = ticker.info
    p = input('Peroid : ')
    i = period_to_interval(p)
    day = ticker.history(period = p, interval = i)
    prices = day['Close'].round(2).tolist()
    change = prices[-1] - prices[0]
    dates = date_selector(day,p)
    title = f'{data["longName"]} | {tickname.upper()}'
    print(f'Day\'s Range : {round(data["dayLow"],2)}-{round(data["dayHigh"],2)}$')
    print(f'Regular Market Price : {round(data["regularMarketPrice"],2)}$')
    return(prices,change,dates,title)


def portfolio_add():
    tick = validate()
    amount = float(input('Enter shares amount : '))
    tick = tick.upper().strip()
    add_one(tick,amount)

def portfolio_delete():
    tick = validate()
    tick = tick.upper().strip()
    delete_one(tick)

def portfolio_view():
    amount = 0
    if l := get_all():
        for elem in l:
            am = round(price_return(elem[0]) * elem[1],2)
            amount+=am
            print(f'{elem[0]} - {elem[1]} [shares] => {am}$')
        print(f'Total worth : {round(amount,2)}$')
    else:
        print('\nPortfolio is empty!\n')

def top_5(asc):
    if asc == False:
        print(f'\nBiggest growth')
    else:
        print(f'\nSmallest growth')
    print('-'*14)
    l = get_top_5(asc)
    for elm in l:
        print(f'{elm[0]} - {color(elm[3])}{elm[3]}%{Style.RESET_ALL}')
    print('\n')

def comp():
    nr = int(input('How many stocks would you like to compare: '))
    l = []
    names = []
    first = True
    while True:
        p = input('Peroid : ').lower().strip()
        if p in ['1d','5d','1mo','6mo','ytd','1y','5y']:
            break
        else:
            print('-INVALID PERIOD-')
    i = period_to_interval(p)
    for _ in range(nr):
        tickname = validate()
        ticker = yf.Ticker(tickname)
        names.append(tickname.upper().strip())
        day = ticker.history(period = p, interval = i)
        prices = day['Close'].round(2).tolist()
        if first:
            dates = date_selector(day,p)
            first = False
        l.append(prices)
    graph_creator2(nr,l,dates,' vs '.join(names),names)

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

def cache_check():
    with sqlite3.connect('cache.db') as conn:
        c= conn.cursor()
        c.execute("SELECT * FROM user_cache")
        print(c.fetchall())

def projector():
    print()
    print(Fore.RED + "THIS IS FOR ENTERTAINMENT PURPOSES" + Style.RESET_ALL + "\n by no means will it be accurate ")
    num = int(input('Enter a time span (years) : '))
    tick = validate()
    usd_inflation = round(pow((1+0.025),num),3)
    print(f'Rate of inflation (aprox 2.5%/year):\n1 USD (today) ≈ {usd_inflation} USD (in {num} years)')
    with sqlite3.connect('cache.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM user_cache WHERE ticker = (?)",(tick,))
        data = c.fetchone()
        rate = data[1]
        price = data[2]
    resp = yes_no(input(f'{tick}\'s last year\'s growth rate was : {rate}% , would you like to add a margin? (yes/no) : '))
    rate /=100
    if resp:
        margin = int(input(r'Margin (e.g. 2 for ±2%): '))
        projected = price
        print(f"\nYearly projections for {tick.upper()} with ±{margin}% margin:")
        year = datetime.now().year
        for i in range(1, num + 1):
            rand_rate = uniform(rate - margin/100, rate + margin/100)
            projected *= (1 + rand_rate)
            year += 1
            print(f'Year {year}: {projected:.2f} USD')
        growth = projected
    else:
        growth = round(price * pow(1 + rate, num), 2)
    print(f'\nProjected growth for {tick.upper()} (based on past performance) : {growth:.2f}')

def menu():
    os.system('cls')
    text = Figlet(font='slant')
    print(text.renderText('Indexized'))
    print("=" * 40)
    print("               MAIN MENU")
    print("=" * 40)
    print(Fore.CYAN + "1. " + Style.RESET_ALL + " Stock general view (graph)")
    print(Fore.CYAN + "2. " + Style.RESET_ALL + " Stock history")
    print(Fore.CYAN + "3. " + Style.RESET_ALL + " Top 5 (last 5 days)")
    print(Fore.CYAN + "4. " + Style.RESET_ALL + " Stock Compare (min 2)")
    print("=" * 40)
    print(Fore.CYAN + "5. " + Style.RESET_ALL + " View portfolio")
    print(Fore.CYAN + "6. " + Style.RESET_ALL + " Manage portfolio")
    print("=" * 40)
    print(Fore.CYAN + "7. " + Style.RESET_ALL + " Investment projector")
    print("=" * 40)
    print(Fore.CYAN + "8. " + Style.RESET_ALL + " Whitelisted funds")
    print(Fore.RED + "9. " + Style.RESET_ALL + " Exit")

def manage_menu():
    print(Fore.GREEN + "\n1. " + Style.RESET_ALL + "View Portfolio")
    print(Fore.CYAN + "2. " + Style.RESET_ALL + "Add Stock")
    print(Fore.CYAN + "3. " + Style.RESET_ALL + "Delete Stock")
    print(Fore.CYAN + "4. " + Style.RESET_ALL + "Reset Portfolio")
    print(Fore.RED + "9. " + Style.RESET_ALL + "EXIT\n")

def main():
    cache()
    os.system('cls')
    while True:
        check()
        menu()
        op = int(input('Select an option : '))
        match op:
            case 1:
                ticker = validate()
                general_info(ticker)

            case 2:
                ticker = validate()
                period = input('Period : ')
                start, end, change, percent = hist(ticker, period)
                print(f'Start : {start}$ -> End : {end}$')
                print(f'{color(percent)}Change : {change}$({percent}%){Style.RESET_ALL}')
                input('Press ENTER to continue...')

            case 3:
                asc = yes_no(input('ASC (smallest growth first) :'))
                top_5(asc)
                input('Press ENTER to continue...')

            case 4:
                comp()
                input('Press ENTER to continue...')

            case 5:
                portfolio_view()
                input('Press ENTER to continue...')

            case 6:
                while True:
                    manage_menu()
                    op2 = int(input(''))
                    match op2:
                        case 1:
                            portfolio_view()
                        case 2:
                            portfolio_add()
                        case 3:
                            portfolio_delete()
                        case 4: 
                            reset()
                        case 9:
                            break
                        case _:
                            print("Invalid option. Try again.")
                portfolio_add()
                input('Press ENTER to continue...')
            case 7 :
                projector()
                input('Press ENTER to continue...')
            case 8:
                all_funds()
                input('Press ENTER to continue...')

            case 9:
                print('Exiting program')
                break

            case 11:
                cache_check()
                input('Press ENTER to continue...')

            case _:
                print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
