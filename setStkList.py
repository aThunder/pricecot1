# setStkList.py

'''
    1. Prompts user to input stock symbols
    2. Can handle blanks (even extra blanks) and commas as separators
    3. Creates List of symbols and sends to setStkCSVFile.py
'''

# import sys

class StkSpecs():

    def __init__(self,ID_NameKey):
        self.ID_NameKey = ID_NameKey
        print("Let's begin")

    def promptForList(self):
        self.list1 = []
        self.list2 = []
        self.list1 = input("Type List of Stocks (separated by spaces): ")
        print(self.list1[1])
        print(self.list1)

    def parseList(self):
        counter=0
        completeList = []
        oneSymbol = ''
        # x =[i for i in self.list1]
        # print(x)

        check = False
        for i in self.list1:
            counter += 1
            # print("current: ",i,counter,len(self.list1))
            if (i == " " or i == ",") and check == True:
                completeList.append(oneSymbol)
                oneSymbol = ''
                check = False
            elif (i == " " or i == ",") and check == False:
                oneSymbol = ''
            else:
                oneSymbol += i
                if counter == len(self.list1):
                    completeList.append(oneSymbol)
                else:
                    check = True

        print(completeList)

    def promptForDates(self):
        self.start1 = input("Start Date (yyyymmdd): ")
        self.end1 = input("End Date (leave blank for latest date): ")

def main():
    ID_NameKey = 0
    a = StkSpecs(ID_NameKey)
    a.promptForList()
    a.parseList()
    # a.promptForDates()

if __name__ == '__main__': main()



