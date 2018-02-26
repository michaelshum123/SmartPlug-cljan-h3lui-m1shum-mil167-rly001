import sqlite3

class dbtool:
    def __init__(self):
        self.conn = sqlite3.connect('potatosalad')
        self.c    = self.conn.cursor()

    def insertRow(self,table, colVals):
        qStr = "INSERT INTO " + str(table) + " VALUES ("
        for c in colVals:
            if c is str:
                qStr += "\'" + c + "\',"
            else:
                qStr += c

        qStr = qStr[:-1]
        qStr += ')'
        print(qStr)
        self.c.execute(qStr)
        self.conn.commit()

    #get rows from a table with num LIMIT
    def getRows(self,table,num):
        qStr = "SELECT * FROM " + table
        if num == -1:
            qStr += ';'
        else:
            qStr += ' LIMIT ' + str(num) + ';'
        print(qStr)
        self.c.execute(qStr)
        self.conn.commit()

    def close(self):
        self.conn.close()

