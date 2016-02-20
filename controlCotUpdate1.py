#controlCotUpdate.py

'''
    1. prompts user to create new SQL table or use existing
       for each specified COT commodity and
       then calls Type1CotFormat.py or Type2CotFormat.py (depending on requirements)
       to to populate SQL table
    2. Which of the 2 files is called depends on the COT format for each specific commodity
    3. Allows for creating new table or updating existing table
'''

import json
import urllib.request
import sqlite3

class BuildCot():

    def __init__(self):
        self.conn = sqlite3.connect('allCotSymbols.db')
        self.c = self.conn.cursor()

    def createSQL(self):
        self.c.execute("DROP TABLE IF EXISTS comboCOT")

        self.c.execute("CREATE TABLE comboCOT (ID INTEGER PRIMARY KEY,ID_NameKey,"
                       "Dataset TEXT,Database TEXT,Name TEXT,Date,OpenInt INTEGER,"
                       "RptableLong INTEGER,RptableShort INTEGER, "
                  "NonRptableLong INTEGER,NonRptableShort INTEGER,UNIQUE (Name,Date))")
        # NetRptable REAL,NetNonRptable REAL

            # db.execute('insert into test(t1, i1) values(?,?)', ('one', 1)) ## sample for format syntax

    def populateTables(self):
        import Type1CotFormat,Type2CotFormat
        stocks = Type1CotFormat.main("https://www.quandl.com/api/v3/datasets/CFTC/TIFF_CME_SC_ALL.json", 1)
        bonds = Type1CotFormat.main("https://www.quandl.com/api/v3/datasets/CFTC/US_F_ALL.json",2)
        gold = Type2CotFormat.main("https://www.quandl.com/api/v3/datasets/CFTC/GC_F_ALL.json",3)
        oil = Type2CotFormat.main("https://www.quandl.com/api/v3/datasets/CFTC/CL_F_ALL.json",4)



def main():
    a = BuildCot()
    print()
    newOrExist = input("Create a new table('c') or use existing table('e')?: ")
    print()
    if newOrExist == 'c':
        print("CAUTION: Creating a new table will delete all current data")
        print()
        doubleCheck = input("Type 'y' to verify you want to create a new table: ")
        if doubleCheck == 'y':
            a.createSQL()
            b = a.populateTables()
        else:
            print("No new table created")
            b = a.populateTables()


if __name__ == '__main__': main()
