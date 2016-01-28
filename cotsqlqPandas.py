import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

class spCOT():

    def __init__(self):
        self.conn = sqlite3.connect('allCot.db')
        self.cursor = self.conn.cursor()
        self.cursor.row_factory = sqlite3.Row
        self.diskEngine = create_engine('sqlite:///allCot.db')




    def queryData(self,criteria):
        self.criteria = criteria
        counter = 1
        self.netReportableList = []

        # for item in self.criteria:
        print("Criteria: ",self.criteria)

        self.intoPandas1 = pd.read_sql_query("SELECT * FROM comboCOT"
                                         " WHERE DATE > '2015-10-01' AND "
                                             "NAME LIKE '{0}'".format(self.criteria),self.diskEngine)

        # print("PandaTest1: ", (self.intoPandas1.values)[3][4])
        # print("PandaTest2: ", self.intoPandas1[['Name','OpenInt']])
    def calcNets(self):
        # df['new_col'] = range(1, len(df) + 1) # format example to add new dataframe column

        self.intoPandas1['NetReportable'] = self.intoPandas1['RptableLong']-self.intoPandas1['RptableShort']
        self.intoPandas1['NetNonReportable'] = self.intoPandas1['NonRptableLong']-self.intoPandas1['NonRptableShort']
        # print(self.intoPandas1)
        # print("WeeklyChg: ", self.intoPandas1['NetReportable'].diff())

    def updateSQLNet(self):
        for i in self.netReportable:
            self.cursor.execute("INSERT INTO comboCOT"
                               "(NetRptable,NetNonRptable)"
                                " VALUES(?,?)",
                                (self.netReportable[counter],self.netNonReportable[counter]))
            self.conn.commit()

        # db.execute("insert into test(t1, i1) values(?,?)", ('one', 1)) ## sample for format syntax

    def innerJoin1(self,criteria1):
        self.criteria1 = criteria1
        self.intoPandasJoin1 = pd.read_sql_query("SELECT comboCOT.NAME,"
                                                 " comboCOT.OPENINT, "
                                                 "comboCOT.DATE,"
                                                 " SPXBONDGOLD.CLOSE,"
                                                 " SPXBONDGOLD.VOL"
                                                 " FROM comboCOT "
                                                 "INNER JOIN SPXBONDGOLD "
                                                 "ON comboCOT.ID_NAMEKEY =  SPXBONDGOLD.ID_NAMEKEY "
                                                 "AND comboCOT.DATE = SPXBONDGOLD.DATE "
                                                 "WHERE comboCOT.DATE > '2016-01-01'"
                                                 "AND NAME LIKE '{0}'".format(self.criteria1),
                                                 self.diskEngine)
        self.intoPandasJoin1['NetReportable'] = self.intoPandas1['RptableLong']-self.intoPandas1['RptableShort']

        print("JOINED: ",self.intoPandasJoin1)



    def plot1(self):
        plt.plot(self.intoPandas1['NetReportable'])
        plt.ylabel("Net Position")
        plt.xlabel("Date")
        plt.title("COT: {0} Net Reportable Position".format(self.criteria))
        plt.show()

    #         # db.execute('insert into test(t1, i1) values(?,?)', ('one', 1)) ## sample for format syntax

def main():
    a = spCOT()
    criteria5 = ['%S&P%']#,'%Gold%','%Bond%','%Oil%']
    for i in criteria5:
        b = a.queryData(i)
        calcs = a.calcNets()
        # c= a.plot1()
        d = a.innerJoin1(i)
if __name__ == '__main__': main()
