
#setStkCSVFile.py


"""Very basic program with no prompts or GUI:
              1. Creates new CSV file or accesses existing file
              2. counts # of rows in file
"""
import pandas.io.data as pullData
import datetime
import time

#############################################################
class setCSVFile():
    def __init__(self,symbol):
        self.symbol = symbol

    def accessSite(self,start,end):
        print('self.symbol: ', self.symbol)
        self.start = start
        self.end = end
        self.timeSeries0 = pullData.DataReader(self.symbol, 'yahoo', self.start, self.end)
        self.timeSeries0 = self.timeSeries0.asfreq('W-TUE')



        print("Entered stxSetFile1b.py to use existing file")
        #alternate way to retrieve data
        #self.timeSeries0 = pd.io.data.get_data_yahoo(symbol, self.start, self.end)
        ##for SP500 in above line only use '%5EGSPC' as symbol
        # self.createCSV

    def createCSV(self):
        self.timeSeries0.to_csv('{0} ohlc.csv'.format(self.symbol))
        self.dataFile = pullData.read_csv('{0} ohlc.csv'.format(self.symbol), index_col='Date',parse_dates=True)
        return self.dataFile

    def useCurrentCSV(self):
        self.dataFile = pullData.read_csv('{0} ohlc.csv'.format(self.symbol), index_col='Date',parse_dates=True)
        #print('self.dataFile print:', self.dataFile[2:3])
        print("Entered stxSetFile1b.py to create new file")
        return self.dataFile

    def countRows(self,csv1):
        self.dayCounter = 0
        #print('csv1: ', csv1)
        for i in range(len(csv1)):
            # print(i)
            self.dayCounter +=1
        print('days in the file:',self.dayCounter)
        return self.dayCounter

#########################################################
#########################################################
def main(symbol,choice1a,startDate1,endDate1,actionSelected):
    a = setCSVFile(symbol)

    if choice1a == 'e' :
        # for i in symbol:
        #     print('iiiiii: ',i)
            csv1 = a.useCurrentCSV()
            return csv1

    if choice1a == 'n':
            # checker = True
        # for i in symbol:
        #     print('iiii: ', i)
            a2 = a.accessSite(startDate1,endDate1)
            csv1 = a.createCSV()


    fileDays = a.countRows(csv1)

startDate = '20151201'
endDate = '20160301'

if __name__ == '__main__': main('spy', 'n',startDate,endDate,'actionSelected')
if __name__ == '__main__': main('gld', 'n',startDate,endDate,'actionSelected')
if __name__ == '__main__': main('tlh', 'n',startDate,endDate,'actionSelected')
if __name__ == '__main__': main('ief', 'n',startDate,endDate,'actionSelected')
if __name__ == '__main__': main('uso', 'n',startDate,endDate,'actionSelected')