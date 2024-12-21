"""_summary_

    Returns:
        _type_: _description_
"""
import sqlite3
import yfinance as yf

# from datetime import datetime

# Function to retrieve stock data and write to database


def retrieve_and_store_stock_data(ticker, start_date_2, end_date_2,
                                  db_name='stock_data.db'):
    """
    Retrieve stock data from Yahoo Finance and store it in an SQLite database.

    Args:
        ticker (str): The stock ticker symbol.
        start_date_2 (str): The start date for
             retrieving stock data (YYYY-MM-DD).
        end_date_2 (str): The end date for retrieving
             stock data (YYYY-MM-DD).
        db_name (str, optional): The name of the SQLite
             database file. Defaults to 'stock_data.db'.

    Returns:
        None
    """
    # Fetch stock data from yfinance
    stock_df = yf.download(ticker, start=start_date_2, end=end_date_2)

    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_prices (
            id INTEGER PRIMARY KEY,
            ticker TEXT,
            date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER
        )
    ''')

    # Insert stock data into the database
    for date, stock_row in stock_df.iterrows():
        cursor.execute(
            '''
            INSERT INTO stock_prices (ticker, date,
            open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                ticker,
                date.strftime('%Y-%m-%d'),
                float(stock_row['Open'].iloc[0]),
                float(stock_row['High'].iloc[0]),
                float(stock_row['Low'].iloc[0]),
                float(stock_row['Close'].iloc[0]),
                int(stock_row['Volume'].iloc[0])
            )
        )
    # Commit and close the connection
    conn.commit()
    conn.close()

# Function to retrieve stock data from the database


def get_stock_data(ticker, start_date_1, end_date_1, db_name='stock_data.db'):
    """
    Retrieve stock data from the database.

    Args:
        ticker (str): The stock ticker symbol.
        start_date_1 (str): The start date for the data retrieval
            in 'YYYY-MM-DD' format.
        end_date_1 (str): The end date for the data retrieval in
             'YYYY-MM-DD' format.
        db_name (str, optional): The name of the SQLite database
          file. Defaults to 'stock_data.db'.

    Returns:
        list: A list of tuples containing the stock data retrieved
             from the database.
    """
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Query stock data from the database
    cursor.execute('''
        SELECT * FROM stock_prices
        WHERE ticker = ? AND date BETWEEN ? AND ?
    ''', (ticker, start_date_1, end_date_1))
    # Fetch all results
    rows = cursor.fetchall()

    # Close the connection
    conn.close()

    return rows


# Example usage
if __name__ == "__main__":
    TICKRER1 = 'AAPL'
    START_DATE = '2023-01-01'
    END_DATE = '2023-1-05'

    # Retrieve and store stock data
    retrieve_and_store_stock_data(TICKRER1, START_DATE, END_DATE)

    # Retrieve stock data from the database
    stock_data = get_stock_data(TICKRER1, START_DATE, END_DATE)
    for row in stock_data:
        print(row)
