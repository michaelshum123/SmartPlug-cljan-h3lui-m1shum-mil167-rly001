import sqlite3

class dbtool:
    def __init__(self):
        self.conn = sqlite3.connect('potatosalad')
        self.conn.row_factory = sqlite3.Row
        self.c    = self.conn.cursor()
        
    def insertRow(self,table, colVals):
        qStr = "INSERT INTO " + str(table) + " VALUES ("
        for c in colVals:
            if type(c) is str:
                qStr += "\'" + str(c) + "\',"
            else:
                qStr += str(c)+','

        qStr = qStr[:-1]
        qStr += ')'
        print(qStr)
        self.c.execute(qStr)
        self.conn.commit()

    #get rows from a table with num LIMIT
    def getRows(self,table,num):
        qStr = "SELECT * FROM " + table
        if num == -1:
            qStr += ' '
        else:
            qStr += ' LIMIT ' + str(num) + ';'
        print(qStr)
        ret = self.c.execute(qStr)
        self.conn.commit()
        return ret.fetchall()
    def close(self):
        self.conn.close()

    #values = [ [col type], [col type] ]
    def makeDB(self,table,values):
        qStr = 'CREATE TABLE '+table + ' ('
        for v in values:
            qStr += v[0] + ' ' + v[1] + ', '
        qStr = qStr[:-2]
        qStr += ');'
        print(qStr)
        self.c.execute(qStr)
        self.conn.commit()
