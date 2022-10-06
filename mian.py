import sqlite3
import yfinance


def add_db(finane_data, ticker_name):
    with sqlite3.connect("finance.db") as con:
        cur = con.cursor()
        for key, row in finane_data.iterrows():
            sql = f"""
                INSERT INTO
                tickers(
                    [date],
                    ticker,
                    [OPEN],
                    high,
                    low,
                    [close],
                    volume)
                VALUES
                    ('{key.strftime("%Y-%m-%d")}',
                     '{ticker_name}',
                     {row["Open"]},
                     {row["High"]},
                     {row["Low"]},
                     {row["Close"]},
                     {row["Volume"]})
                """
            try:
                cur.execute(sql)
            except sqlite3.IntegrityError:
                print("IntegrityError: ", key, row)
    con.commit()


ticker_list = ["ES=F", "ZB=F"]
for ticker in ticker_list:
    data = yfinance.download(ticker, period="3y", interval="1wk")
    add_db(data, ticker)
