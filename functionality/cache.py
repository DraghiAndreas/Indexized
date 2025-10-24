from datetime import date

import sqlite3
import yfinance as yf
import numpy as np

current_date = date.today()

def init_db():
    with sqlite3.connect('cache.db') as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS last_update(
                id INTEGER PRIMARY KEY,
                data TEXT
                )
            """)

def get_last_update():
    with sqlite3.connect('cache.db') as conn:
        c = conn.cursor()
        c.execute('SELECT data FROM last_update WHERE id = 1')
        row = c.fetchone()
        if row:
            return date.fromisoformat(row[0])
        return None

def set_last_update(new_date):
    with sqlite3.connect('cache.db') as conn:
        c = conn.cursor()
        c.execute("UPDATE last_update SET data = (?) WHERE id = 1", (str(new_date),))
        if c.rowcount == 0:
            c.execute("INSERT INTO last_update(id, data) VALUES (1,?)",(str(new_date),))


def cache():
    init_db()

    last_updt = get_last_update()
    if last_updt == current_date:
        return 0

    tickers_str = "VTI SPY VOO SCHB VXUS IXUS VEU BND AGG XLK VNQ DIA QQQ XLF XLE XLY XLI XLV XLC XLU XLB XLRE VIXY SH SQQQ ARKK SOXX EURUSD=X JPYUSD=X GBPUSD=X CNYUSD=X CHFUSD=X"
    data = yf.download(tickers_str, period="1y", interval="1mo")
    data5 = yf.download(tickers_str,period="5d",interval="15m")

    with sqlite3.connect('cache.db') as conn:
        c=conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS user_cache(
                ticker TEXT PRIMARY KEY,
                pct REAL,
                last_price REAL,
                day_5 REAL,
                change5 REAL
                )
            """)
        for tick in tickers_str.split():
            if tick in ('GBPUSD=X','EURUSD=X','JPYUSD=X','CNYUSD=X','CHFUSD=X'):
                rnd = 4
            else:
                rnd = 2

            closes = data['Close'][tick].dropna().to_numpy()

            start = closes[0]
            end = closes[-1]

            pct_change = ((end - start) / start) * 100

            closes5 = data5['Close'][tick].dropna().to_numpy()
            start5 = closes5[0]

            pct_change5 = ((end - start5) / start5) * 100
            change5 = end-start5
            print(f'{tick} | start : {start} | end : {end} | percent (last year) : {pct_change} | start (5 days): {start5} | change (5 days) : {change5} | percent (5 days) : {pct_change5}')
            c.execute("INSERT OR REPLACE INTO user_cache(ticker,pct,last_price, day_5,change5) VALUES (?,?,?,?,?)",(tick,round(pct_change,rnd),round(end,rnd),round(pct_change5,rnd),round(change5,rnd)))
        print('-DATA CACHED SUCCESSFULLY-')
    set_last_update(current_date)
