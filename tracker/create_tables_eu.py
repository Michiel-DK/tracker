import psycopg2
from tracker.postgres import connect, config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE yearly_financials (
                index BIGINT,
                year BIGINT,
                accountspayable BIGINT,
                assetturnover REAL,
                capitalexpenditures BIGINT,
                capitalsurplus BIGINT,
                cash BIGINT,
                cashdebt REAL,
                cashflow BIGINT,
                changeincash BIGINT,
                changetoaccountreceivables BIGINT,
                changetoinventory BIGINT,
                changetoliabilities BIGINT,
                changetonetincome BIGINT,
                changetooperatingactivities BIGINT,
                commonstock BIGINT,
                currentratio REAL,
                debtequity REAL,
                deferredlongtermassetcharges BIGINT,
                deferredlongtermliab BIGINT,
                depreciation BIGINT,
                dividendspaid BIGINT,
                earnings BIGINT,
                effectofexchangerate BIGINT,
                equityasset REAL,
                equitymultipl REAL,
                fcf BIGINT,
                fcfmargin REAL,
                financialleverage REAL,
                goodwill BIGINT,
                goodwillassets REAL,
                intangibleassets BIGINT,
                inventory BIGINT,
                investments BIGINT,
                issuanceofstock BIGINT,
                longtermdebt BIGINT,
                longterminvestments BIGINT,
                minorityinterest BIGINT,
                netborrowings BIGINT,
                netincome BIGINT,
                netmargin REAL,
                netreceivables BIGINT,
                nettangibleassets BIGINT,
                operatingmargin REAL,
                otherassets BIGINT,
                othercashflowsfromfinancingactivities BIGINT,
                othercashflowsfrominvestingactivities BIGINT,
                othercurrentassets BIGINT,
                othercurrentliab BIGINT,
                otherliab BIGINT,
                otherstockholderequity BIGINT,
                propertyplantequipment BIGINT,
                receivablessales REAL,
                repurchaseofstock BIGINT,
                retainedearnings BIGINT,
                revenue BIGINT,
                roa REAL,
                roe REAL,
                roic REAL,
                shortlongtermdebt BIGINT,
                shortterminvestments BIGINT,
                ticker VARCHAR(8),
                totalassets BIGINT,
                totalcashflowsfrominvestingactivities BIGINT,
                totalcashfromfinancingactivities BIGINT,
                totalcashfromoperatingactivities BIGINT,
                totalcurrentassets BIGINT,
                totalcurrentliabilities BIGINT,
                totalliab BIGINT,
                totalstockholderequity BIGINT,
                treasurystock BIGINT
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