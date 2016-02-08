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
        self.recentList =[]

    def innerJoin1(self,criteria1):
        self.criteria1 = criteria1
        self.intoPandasJoin1 = pd.read_sql_query("SELECT comboCOT.NAME,"
                                                 " comboCOT.OPENINT, "
                                                 "comboCOT.DATE,"
                                                 " comboCOT.RptableLong,"
                                                 " comboCOT.RptableShort,"
                                                 "SPXBONDGOLD.SYMBOL,"
                                                 " SPXBONDGOLD.CLOSE,"
                                                 " SPXBONDGOLD.VOL, "
                                                 "SPXBONDGOLD.DATE "
                                                 " FROM comboCOT "
                                                 "INNER JOIN SPXBONDGOLD "
                                                 "ON comboCOT.ID_NAMEKEY =  SPXBONDGOLD.ID_NAMEKEY "
                                                 "AND comboCOT.DATE = SPXBONDGOLD.DATE "
                                                 "WHERE comboCOT.DATE > '2015-12-15'"
                                                 "AND NAME LIKE '{0}'"
                                                 "ORDER BY SPXBONDGOLD.DATE asc".format(self.criteria1),
                                                 self.diskEngine)

        countLinesAll = self.intoPandasJoin1['Date'].count()
        self.intoPandasJoin1['NetReportable'] = self.intoPandasJoin1['RptableLong']-self.intoPandasJoin1['RptableShort']
        self.intoPandasJoin1['WkNetRptableChg'] = self.intoPandasJoin1['NetReportable'].diff()
        self.intoPandasJoin1['WkPriceChg'] = np.round(self.intoPandasJoin1['close'].diff(),decimals=2)

        print("JOINED: ",self.intoPandasJoin1)

    def mostRecent(self):

        countLines = self.intoPandasJoin1['WkNetRptableChg'].count()
        print('#Lines: ',countLines)
        mostRecent = ("{0}: NetReportable: {1}  WeeklyChg: {2} WkPriceChg: {3}".
                format(self.intoPandasJoin1['Symbol'][countLines],self.intoPandasJoin1['NetReportable'][countLines],
                self.intoPandasJoin1['WkNetRptableChg'][countLines],self.intoPandasJoin1['WkPriceChg'][countLines]))

        # print("MostRecent {0}: {1}".
        #         format(self.criteria1,mostRecent))

        self.recentList.append(mostRecent)

    def summary1(self):
        print()
        counter=1
        for i in self.recentList:
            print(counter, i)
            counter +=1

    def plot1(self):
        plt.plot(self.intoPandas1['NetReportable'])
        plt.ylabel("Net Position")
        plt.xlabel("Date")
        plt.title("COT: {0} Net Reportable Position".format(self.criteria))
        plt.show()

    #         # db.execute('insert into test(t1, i1) values(?,?)', ('one', 1)) ## sample for format syntax

def main():
    a = spCOT()
    criteria5 = ['%S&P%','%Gold%','%Bond%','%Oil%']
    for i in criteria5:
        a.innerJoin1(i)
        a.mostRecent()
    a.summary1()
        # c= a.plot1()

if __name__ == '__main__': main()



############
 # def updateSQLNet(self):
    #     for i in self.netReportable:
    #         self.cursor.execute("INSERT INTO comboCOT"
    #                            "(NetRptable,NetNonRptable)"
    #                             " VALUES(?,?)",
    #                             (self.netReportable[counter],self.netNonReportable[counter]))
    #         self.conn.commit()
    #
    #     # db.execute("insert into test(t1, i1) values(?,?)", ('one', 1)) ## sample for format syntax

############
# def queryData(self,criteria):
    #     self.criteria = criteria
    #     counter = 1
    #     self.netReportableList = []
    #
    #     # for item in self.criteria:
    #     print("Criteria: ",self.criteria)
    #
    #     self.intoPandas1 = pd.read_sql_query("SELECT NAME,DATE,RPTABLELONG,RPTABLESHORT FROM comboCOT"
    #                                      " WHERE DATE > '2015-12-31' AND "
    #                                          "NAME LIKE '{0}'"
    #                                          " ORDER BY DATE".format(self.criteria),self.diskEngine)
    #
    #     # print("PandaTest1: ", (self.intoPandas1.values))
    #     # print("PandaTest1: ", (self.intoPandas1.values)[4][5])
    #     # print("PandaTest2: ", self.intoPandas1[['Name','OpenInt']])
    # def calcNets(self):
    #     # df['new_col'] = range(1, len(df) + 1) # general format example to add new dataframe column
    #
    #     # self.intoPandas1['NetReportable'] = self.intoPandas1['RptableLong']-self.intoPandas1['RptableShort']
    #     # print('NetReportable: ',self.intoPandas1['NetReportable'])
    #     # self.intoPandas1['NetNonReportable'] = self.intoPandas1['NonRptableLong']-self.intoPandas1['NonRptableShort']
    #     # self.intoPandas1['WeeklyNetRptableChg'] = self.intoPandas1['NetReportable'].diff()
    #     # # print(self.intoPandas1)
    #     print("WeeklyChg: ", self.intoPandas1['NetReportable'].diff())
