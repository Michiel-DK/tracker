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
    df.to_csv(buffer, index_label='id', header=False)
    buffer.seek(0)
    # read database configuration
    params = config()
    # connect to the PostgreSQL database
    conn = psycopg2.connect(**params)
    # create a new cursor    
    cursor = conn.cursor()
    try:
        cursor.copy_from(buffer, table, sep=",")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("copy_from_stringio() done")
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
    tickers = ['ABBV','ADBE', 'AMGN', 'AY', 'BABA', 'CARM.PA', 'CRM', 'CRSP', 'CVS', 'DUKE.L', 'EURN', 'GAIN', 'GOOGL', 'HASI', 'HSI', 'HHFA.DE', 'NXR.L', 'MO', "MSFT", 'PLTR', 'PYPL', 'RDS-A', 'SQ', 'TCPC', 'TDOC', "TSLX", 'TCPC', 'TTE', 'TRI.PA','V' , "WEHB.BR"]
    start = time.time()
    print(start)
    for ticker in tickers:
        full = Yahoo(ticker)
        fundamentals = full.add_fundamentals()
        copy_from_stringio(fundamentals, 'yearly_financials')
        moat, health = full.checklist()
        copy_from_stringio(moat, 'yearly_moat')
        copy_from_stringio(health, 'yearly_health')
    end = time.time()-start
    print(end)