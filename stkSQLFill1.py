
import sqlite3
import csv
# import sys

class Csv2SQL():

    def __init__(self,symbol,ID_NameKey):
        self.symbol = symbol
        self.ID_NameKey = ID_NameKey

        self.conn = sqlite3.connect('allCOT.db')
        self.c=self.conn.cursor()
        # self.keyFiller = 1

    def createTables(self):

        for i in self.symbol:

            print(i)
            self.c.execute("DROP TABLE IF EXISTS SPXBONDGOLD")

            ### Following uses ID as only PRIMARY KEY in order to get ID to autoincrement
            self.c.execute("CREATE TABLE SPXBONDGOLD(ID INTEGER PRIMARY KEY, ID_NameKey INTEGER,Symbol CHAR,date, "
                           "open real,high real ,low real,close real ,vol int ,adjclose real)")

            # self.index1 = self.c.execute("CREATE INDEX INDEXKEY ON StxData2(date)")
            # self.index2 = self.c.execute("CREATE UNIQUE INDEX INDEXDATE ON StxData2(keynumber)")

    def populateTables(self):
        for i in self.symbol:
            rowNumber=0
            with open('{0} ohlc.csv'.format(i), newline='') as csvfile:
              reader = csv.reader(csvfile, delimiter=',', quotechar='|')
              for row in reader:
                if rowNumber > 0:

                  # print(self.keyFiller,i,row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                  self.c.execute("INSERT OR IGNORE INTO SPXBONDGOLD (ID_NameKey,symbol, date,"
                                 "open,high ,low ,close ,vol ,adjclose ) VALUES (?,?,?,?,?,?,?,?,?)",
                                 (self.ID_NameKey,i,row[0],row[1],row[2],row[3],row[4],row[5],row[6]))


                  # self.c.execute("REPLACE INTO StxData2 (keynumber, symbol, date,open,high ,low ,close ,vol ,adjclose ) VALUES (?,?,?,?,?,?,?,?,?)", (self.keyFiller,i,row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                else:
                    rowNumber += 1
              self.conn.commit()

              # print('SQL Table Updated')

              # cursor3 = conn.execute("SELECT date, close from Stock"+ i + " ORDER BY date")
              # for row in cursor3:
              #     print(row)
        roww = self.c.lastrowid
        print(roww)

    def printMessage(self,whichOne):
        if whichOne == 'b':
            print("SQL Table Created")
        else:
            print("SQL Table Updated")
        # self.c.execute(select count(*) from <stxTable1> where ..


def start(symbols,createOrUpdate,ID_NameKey):
    print(symbols)
    # chooseTable = input("Add to existing Table ('a') or create new Table ('c')?: ")
    a = Csv2SQL(symbols,ID_NameKey)
    if createOrUpdate== 'c':
        b = a.createTables()
        c= a.populateTables()
    elif createOrUpdate == 'e':
        c = a.populateTables()
    else:
        print("Invalid Response. Try Again")
        start(symbols)
    d = a.printMessage(createOrUpdate)

start(['SPY'], 'c',1)
start(['GLD'], 'e',3)
start(['TLH'], 'e',2)
# start(['IEF'], 'e',2)
start(['USO'], 'e',4)
