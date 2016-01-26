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
        self.netReportable = self.intoPandas1['RptableLong']-self.intoPandas1['RptableShort']
        self.netNonReportable = self.intoPandas1['NonRptableLong']-self.intoPandas1['NonRptableShort']
        print(self.netReportable)#, self.netNonReportable)
        print("WeeklyChg: ", self.netReportable.diff())

    def innerJoin1(self,criteria1):
        self.criteria1 = criteria1
        self.intoPandasJoin1 = pd.read_sql_query("SELECT comboCOT.NAME,"
                                                 " SPXBONDGOLD.CLOSE"
                                                 " FROM comboCOT "
                                                 "INNER JOIN SPXBONDGOLD "
                                                 "ON comboCOT.ID_NAMEKEY =  SPXBONDGOLD.ID_NAMEKEY",self.diskEngine)
        print("JOINED: ",self.intoPandasJoin1)

                                              #       "SELECT employees.employee_id,"
                                              # " employees.last_name,"
                                              # " positions.title"
                                              # " FROM employees "
                                              # "INNER JOIN positions "
                                              # "ON employees.position_id = positions.position_id"



    def plot1(self):
        plt.plot(self.netReportable)
        plt.ylabel("Net Position")
        plt.xlabel("Date")
        plt.title("COT: {0} Net Reportable Position".format(self.criteria))
        plt.show()

    #         # db.execute('insert into test(t1, i1) values(?,?)', ('one', 1)) ## sample for format syntax

def main():
    a = spCOT()
    criteria5 = ['%S&P%','%Gold%','%Bond%','%Oil%']
    for i in criteria5:
        # b = a.queryData(i)
        # calcs = a.calcNets()
        # c= a.plot1()
        d = a.innerJoin1(i)
if __name__ == '__main__': main()
