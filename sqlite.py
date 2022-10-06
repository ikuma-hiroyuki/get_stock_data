import sqlite3

with sqlite3.connect("finance.db") as cn:
    cur = cn.cursor()
    try:
        cur.execute("drop table tickers")
    except sqlite3.OperationalError:
        pass
    finally:
        create_tb = """
            CREATE TABLE tickers(
            [date] DATE,
            ticker TEXT,
            [open] REAL,
            high REAL,
            low REAL,
            [close] REAL,
            volume INTEGER,
            PRIMARY KEY(date, ticker))
            """
    cur.execute(create_tb)
    cn.commit()
