import psycopg2
from tracker.postgres import connect, config
import pandas as pd

params = config(filename='/Users/admin/code/Michiel-DK/tracker/database.ini', section='postgresql')

conn = psycopg2.connect(**params)

def get_quarterly_moat(ticker):
    cur = conn.cursor()
    cur.execute(f"""SELECT * from quarterly_moat WHERE ticker = '{ticker}'""")
    selected_moat = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    selected_moat_df = pd.DataFrame(selected_moat, columns=colnames).drop(columns='index')
    cur.close();
    return selected_moat_df

def get_quarterly_health(ticker):
    cur = conn.cursor()
    cur.execute(f"""SELECT * from quarterly_health WHERE ticker = '{ticker}'""")
    selected_moat = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    selected_health_df = pd.DataFrame(selected_moat, columns=colnames).drop(columns='index')
    cur.close();
    return selected_health_df


def get_yearly_moat(ticker):
    cur = conn.cursor()
    cur.execute(f"""SELECT * from yearly_moat WHERE ticker = '{ticker}'""")
    selected_moat = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    selected_moat_df = pd.DataFrame(selected_moat, columns=colnames).drop(columns='index')
    cur.close();
    return selected_moat_df

def get_yearly_health(ticker):
    cur = conn.cursor()
    cur.execute(f"""SELECT * from yearly_health WHERE ticker = '{ticker}'""")
    selected_moat = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    selected_health_df = pd.DataFrame(selected_moat, columns=colnames).drop(columns='index')
    cur.close();
    return selected_health_df