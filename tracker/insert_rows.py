import psycopg2
from tracker.postgres import connect, config
from tracker.data_yahoo import Yahoo
from io import StringIO
import time

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
    #tickers = ['ABBV','ADBE', 'AMGN', 'AY', 'BABA', 'CARM.PA', 'CRM', 'CRSP', 'CVS', 'DUKE.L', 'EURN', 'GAIN', 'GOOGL', 'HASI', 'NXR.L', 'MO', "MSFT", 'PYPL', 'RDS-A', 'SQ', 'TCPC', 'TDOC', "TSLX", 'TCPC', 'TTE', 'TRI.PA','V', 'LMT', 'RTX', 'IIPR', 'MCO', 'TMO', 'APO', 'ABT', 'TROW', 'WSM', 'KMI', 'OKE']
    tickers = ['AAPL', 'AKAM', 'AVGO', 'AMZN', 'SHOP', 'TWLO', 'MDB', 'MELI', 'FB', 'KLIC', 'QCOM']
    start = time.time()
    for ticker in tickers:
        full = Yahoo(ticker)
        try:
            individ = time.time()
            fundamentals = full.get_fundamentals()
            copy_from_stringio(fundamentals, 'yearly_financials')
            moat, health = full.get_checklist()
            copy_from_stringio(moat, 'yearly_moat')
            copy_from_stringio(health, 'yearly_health')
            info = full.get_info()
            copy_from_stringio(info, 'weekly_info')
            print(f"time for {ticker} : {time.time() - individ}")
            individ = time.time()-individ
        except AttributeError:
            print(f'Attribute error for {ticker}')
            pass
    end = time.time()-start
    print(f"total run-time: {end/60} min")