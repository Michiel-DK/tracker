import psycopg2
from yfinance import Tickers
from tracker.postgres import connect, config
from tracker.tickers import get_tickers
import numpy as np
from tracker.data_yahoo import Yahoo
from io import StringIO
import time
import sys


def copy_from_stringio(df, table):
    """
    Here we are going save the dataframe in memory 
    and use copy_from() to copy it to the table
    """
    # save dataframe to an in memory buffer
    buffer = StringIO()
    df.to_csv(buffer, index_label='id', header=False, sep=";")
    buffer.seek(0)
    # read database configuration
    params = config()
    # connect to the PostgreSQL database
    conn = psycopg2.connect(**params)
    # create a new cursor    
    cursor = conn.cursor()
    try:
        cursor.copy_from(buffer, table, sep=";", null='')
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()

# def insert_one(row):
#     """ insert a new vendor into the vendors table """
#     sql = """INSERT INTO vendors(vendor_name)
#              VALUES(%s) RETURNING vendor_id;"""
#     conn = None
#     vendor_id = None
#     try:
#         # read database configuration
#         params = config()
#         # connect to the PostgreSQL database
#         conn = psycopg2.connect(**params)
#         # create a new cursor
#         cur = conn.cursor()
#         # execute the INSERT statement
#         cur.execute(sql, (row,))
#         # get the generated id back
#         vendor_id = cur.fetchone()[0]
#         # commit the changes to the database
#         conn.commit()
#         # close communication with the database
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()

#     return vendor_id

# def insert_multiple(rows):
#     """ insert multiple vendors into the vendors table  """
#     sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
#     conn = None
#     try:
#         # read database configuration
#         params = config()
#         # connect to the PostgreSQL database
#         conn = psycopg2.connect(**params)
#         # create a new cursor
#         cur = conn.cursor()
#         # execute the INSERT statement
#         cur.executemany(sql,rows)
#         # commit the changes to the database
#         conn.commit()
#         # close communication with the database
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
            
            
if __name__ == '__main__':
    start = time.time()
    not_found_q = []
    time_q = []
    not_found_y = []
    time_y = []
    not_found_i = []
    time_i = []
    tickers = get_tickers()
    third = round(len(tickers)/3)
    select = tickers[third:third*2]
    for ticker in select:
        full = Yahoo(ticker, timing='q')
        try:
            individ = time.time()
            fundamentals = full.get_fundamentals()
            copy_from_stringio(fundamentals, 'quarterly_financials')
            moat, health = full.get_checklist()
            copy_from_stringio(moat, 'quarterly_moat')
            copy_from_stringio(health, 'quarterly_health')
            growth = full.get_growth()
            copy_from_stringio(growth, 'quarterly_growth')
            #print(f"time for q {ticker} : {time.time() - individ}")
            print(f"q - {ticker}")
            time_q.append(time.time() - individ)
        except AttributeError:
                print(f'Attribute error for q {ticker}')
                not_found_q.append(ticker)
                pass
        except KeyError:
                print(f'Key error for q {ticker}')
                not_found_q.append(ticker)
                pass

    start = time.time()
    print("y")
    for ticker in select:
        full = Yahoo(ticker)
        try:
            individ = time.time()
            fundamentals = full.get_fundamentals()
            copy_from_stringio(fundamentals, 'yearly_financials')
            moat, health = full.get_checklist()
            copy_from_stringio(moat, 'yearly_moat')
            copy_from_stringio(health, 'yearly_health')
            growth = full.get_growth()
            copy_from_stringio(growth, 'yearly_growth')
            #print(f"time for y {ticker} : {time.time() - individ}")
            print(f"y - {ticker}")
            time_y.append(time.time() - individ)
        except AttributeError:
                print(f'Attribute error for y {ticker}')
                not_found_y.append(ticker)
                pass
        except KeyError:
                print(f'Key error for y {ticker}')
                not_found_y.append(ticker)
                pass
    
    print("i")
    start = time.time()
    for ticker in select:
        full = Yahoo(ticker)
        try:
            individ = time.time()
            info = full.get_info()
            copy_from_stringio(info, 'weekly_info')
            #print(f"time for i {ticker} : {time.time() - individ}")
            time_i.append(time.time() - individ)
            print(f"i - {ticker}")
        except AttributeError:
                print(f'Attribute error for i {ticker}')
                not_found_i.append(ticker)
                pass
        except KeyError:
                print(f'Key error for i {ticker}')
                not_found_i.append(ticker)
                pass
    end = time.time()-start
    print(f"total run-time info: {end/60} min")
    print(f"total time q {sum(time_q)/60}, avg time q {np.mean(time_q)}")
    print(f"not found q {not_found_q}")
    print(f"total time y {sum(time_y)/60}, avg time y {np.mean(time_y)}")
    print(f"not found y {not_found_y}")
    print(f"total time i {sum(time_i)/60}, avg time i {np.mean(time_i)}")
    print(f"not found i {not_found_i}")