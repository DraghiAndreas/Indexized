import sqlite3

def check():
    with sqlite3.connect('portfolio.db') as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS user_portfolio(
                ticker TEXT UNIQUE,
                amount REAL
            )
        """)

def save_user(username):
    with sqlite3.connect('portfolio.db') as conn:
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            username TEXT
        )
        ''')
        c.execute('SELECT COUNT(*) FROM user_data')
        count = c.fetchone()[0]
        
        if count == 0:
            c.execute('INSERT INTO user_data (username) VALUES (?)', (username,))
        else:
            c.execute('UPDATE user_data SET username = ?', (username,))
        
        conn.commit()

def get_username():
	with sqlite3.connect('portfolio.db') as conn:
		c = conn.cursor()
		c.execute('SELECT name FROM sqlite_master WHERE type = "table" and name="user_data"')
		if not c.fetchone():
			return None
		
		c.execute("SELECT username FROM user_data")
		username = c.fetchone()
		return username[0]

def get_all():
	with sqlite3.connect('portfolio.db') as conn:
		c = conn.cursor()
		c.execute("SELECT * FROM user_portfolio")
		return c.fetchall()

def add_one(tickerN,amountN):
	with sqlite3.connect('portfolio.db') as conn:
		c = conn.cursor()
		c.execute("""
			INSERT INTO user_portfolio(ticker,amount) VALUES (?,?) 
			ON CONFLICT (ticker) DO UPDATE SET amount = amount + excluded.amount
			""",(tickerN,amountN))

def delete_one(tickerN):
	with sqlite3.connect('portfolio.db') as conn:
		c = conn.cursor()
		c.execute("DELETE FROM user_portfolio WHERE ticker = (?)",(tickerN,))
		if c.rowcount:
			print(f'{tickerN} DELETED')
		else:
			print(f"{tickerN} DOESN'T EXIST")

def reset():
	with sqlite3.connect('portfolio.db') as conn:
		c = conn.cursor()
		c.execute("DROP TABLE user_portfolio")

def get_currencies():
	with sqlite3.connect('cache.sql') as conn:
		c = conn.cursor()
		c.execute('Select *  FROM user_cache WHERE ticker IN ("EURUSD=X","JPYUSD=X","GBPUSD=X","CNYUSD=X","CHFUSD=X") ORDER BY day_5 DESC')
		return c.fetchall()

def get_top_5(asc):
	with sqlite3.connect('cache.sql') as conn:
		c=conn.cursor()
		if(asc):
			c.execute("SELECT * FROM user_cache WHERE ticker NOT IN ('CHFUSD=X','EURUSD=X','JPYUSD=X','GBPUSD=X','CNYUSD=X') ORDER BY day_5 ASC LIMIT 5")
		else:
			c.execute("SELECT * FROM user_cache WHERE ticker NOT IN ('CHFUSD=X','EURUSD=X','JPYUSD=X','GBPUSD=X','CNYUSD=X') ORDER BY day_5 DESC LIMIT 5")
	

		return c.fetchall()