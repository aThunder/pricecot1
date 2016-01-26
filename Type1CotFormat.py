import json
import urllib.request
import sqlite3

class Type1():

    def __init__(self,url,ID_NameKey):
        self.url = url
        self.ID_NameKey = ID_NameKey
        self.conn = sqlite3.connect('allCot.db')
        self.c = self.conn.cursor()

    def getData(self):
        openURL = urllib.request.urlopen(self.url)
        readURL = openURL.read()
        self.datax = json.loads(readURL.decode("utf8"))

        print("TTL Reportable Long: ",self.datax['dataset']['data'][0][14])
        print("TTL Reportable Short: ",self.datax['dataset']['data'][0][15])
        print("Non-Reportable Long: ",self.datax['dataset']['data'][0][16])
        print("Non-Reportable Short: ",self.datax['dataset']['data'][0][17])

    def populateSQL(self):
        counter = 0
        for line in self.datax['dataset']['data'][0:]: # [0:] range added to allow for specifying range limits to iterate
            # print('day: ',line)

            self.c.execute("INSERT OR IGNORE INTO comboCOT"
                           "(ID_NameKey,Dataset,Database,Name,Date,OpenInt,RptableLong,"
                           "RptableShort,NonRptableLong,NonRptableShort)"
                            " VALUES(?,?,?,?,?,?,?,?,?,?)",
                            (self.ID_NameKey,
                            self.datax['dataset']['dataset_code'],
                            self.datax['dataset']['database_code'],
                            self.datax['dataset']['name'],
                            self.datax['dataset']['data'][counter][0],
                            self.datax['dataset']['data'][counter][1],
                            self.datax['dataset']['data'][counter][14],
                            self.datax['dataset']['data'][counter][15],
                            self.datax['dataset']['data'][counter][16],
                            self.datax['dataset']['data'][counter][17]))

            counter += 1
            self.conn.commit()

            # db.execute('insert into test(t1, i1) values(?,?)', ('one', 1)) ## sample for format syntax

def main(url,ID_NameKey):
    print('xxxx: ',ID_NameKey)
    a = Type1(url,ID_NameKey)
    a.getData()
    a.populateSQL()
    return

if __name__ == '__main__': main(url,ID_NameKey)

