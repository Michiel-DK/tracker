import psycopg2
from tracker.postgres import connect, config


def create_tables():
    """ create tables in the PostgreSQL database"""
    command = (
        """
        CREATE TABLE financials (
            index INT,
            ebitda BIGINT,
            accountspayable BIGINT,
            capitalsurplus BIGINT,
            cashchange BIGINT,
            cashflow BIGINT,
            cashflowfinancing BIGINT,
            changesininventories BIGINT,
            changesinreceivables BIGINT,
            commonstock BIGINT,
            costofrevenue BIGINT,
            currency VARCHAR(3),
            currentassets BIGINT,
            currentcash BIGINT,
            currentdebt BIGINT,
            currentlongtermdebt BIGINT,
            depreciation BIGINT,
            dividendspaid BIGINT,
            ebit BIGINT,
            exchangerateeffect BIGINT,
            filingtype VARCHAR(4),
            fiscaldate VARCHAR(6),
            fiscalquarter BIGINT,
            fiscalyear BIGINT,
            goodwill BIGINT,
            grossprofit BIGINT,
            incometax BIGINT,
            intangibleassets BIGINT,
            interestincome BIGINT,
            inventory BIGINT,
            investingactivityother BIGINT,
            investments BIGINT,
            longtermdebt BIGINT,
            longterminvestments BIGINT,
            minorityinterest BIGINT,
            netborrowings BIGINT,
            netincome BIGINT,
            netincomebasic BIGINT,
            nettangibleassets BIGINT,
            operatingexpense BIGINT,
            operatingincome BIGINT,
            operatingrevenue BIGINT,
            otherassets BIGINT,
            othercurrentassets BIGINT,
            othercurrentliabilities BIGINT,
            otherincomeexpensenet BIGINT,
            otherliabilities BIGINT,
            pretaxincome BIGINT,
            propertyplantequipment BIGINT,
            receivables BIGINT,
            reportdate VARCHAR(10),
            researchanddevelopment BIGINT,
            retainedearnings BIGINT,
            revenue BIGINT,
            sellinggeneralandadmin BIGINT,
            shareholderequity BIGINT,
            shorttermdebt BIGINT,
            shortterminvestments BIGINT,
            symbol VARCHAR(5),
            totalassets BIGINT,
            totalcash BIGINT,
            totaldebt BIGINT,
            totalinvestingcashflows BIGINT,
            totalliabilities BIGINT,
            totalrevenue BIGINT,
            treasurystock BIGINT,
            id VARCHAR(10),
            key VARCHAR(4),
            subkey VARCHAR(10),
            date BIGINT,
            updated BIGINT,
            ticker VARCHAR(4),
            fcf BIGINT,
            operating_margin REAL,
            net_margin REAL,
            asset_turnover REAL,
            roa REAL,
            equity_multipl REAL,
            roe REAL,
            fcf_margin REAL,
            cash_debt REAL,
            equity_asset REAL,
            debt_equity REAL,
            debt_ebitda REAL
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        #for command in commands:
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()