import psycopg2
from tracker.postgres import connect, config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE yearly_financials (
            index INT,
            year REAL,
            changetoliabilities BIGINT,
            totalcashflowsfrominvestingactivities BIGINT,
            netborrowings BIGINT,
            totalcashfromfinancingactivities BIGINT,
            changetooperatingactivities BIGINT,
            issuanceofstock BIGINT,
            netincome BIGINT,
            changeincash BIGINT,
            effectofexchangerate BIGINT,
            totalcashfromoperatingactivities BIGINT,
            depreciation BIGINT,
            dividendspaid BIGINT,
            changetoinventory BIGINT,
            changetoaccountreceivables BIGINT,
            othercashflowsfromfinancingactivities BIGINT,
            changetonetincome BIGINT,
            capitalexpenditures BIGINT,
            repurchaseofstock BIGINT,
            intangibleassets BIGINT,
            capitalsurplus BIGINT,
            totalliab BIGINT,
            totalstockholderequity BIGINT,
            minorityinterest BIGINT,
            othercurrentliab BIGINT,
            totalassets BIGINT,
            commonstock BIGINT,
            othercurrentassets BIGINT,
            otherliab BIGINT,
            goodwill BIGINT,
            treasurystock BIGINT,
            otherassets BIGINT,
            cash BIGINT,
            totalcurrentliabilities BIGINT,
            deferredlongtermassetcharges BIGINT,
            shortlongtermdebt BIGINT,
            otherstockholderequity BIGINT,
            propertyplantequipment BIGINT,
            totalcurrentassets BIGINT,
            longterminvestments BIGINT,
            nettangibleassets BIGINT,
            netreceivables BIGINT,
            longtermdebt BIGINT,
            inventory BIGINT,
            accountspayable BIGINT,
            revenue BIGINT,
            earnings BIGINT,
            ticker VARCHAR(8),
            cashflow BIGINT,
            fcf BIGINT,
            operatingmargin REAL,
            netmargin REAL,
            fcfmargin REAL,
            assetturnover REAL,
            roa REAL,
            roe REAL,
            equitymultipl REAL,
            cashdebt REAL,
            equityasset REAL,
            debtequity REAL,
            financialleverage REAL,
            currentratio REAL,
            goodwillassets REAL,
            receivablessales REAL
        )
        """,
        """ CREATE TABLE yearly_moat (
                index INT,
                operatingmargin REAL,
                fcfmargin REAL,
                netmargin REAL,
                roa REAL,
                roe REAL,
                moatpercentage REAL,
                year REAL,
                ticker VARCHAR(8)
        )
        """,
        """CREATE TABLE yearly_health (
                index INT,
                receivablessales REAL,
                currentratio REAL,
                financialleverage REAL,
                debtequity REAL,
                percentage REAL,
                year REAL,
                ticker VARCHAR(8)
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
        for command in commands:
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