#import MySQLdb

class DB:
    def __init__(self):
        self.ip = '0.0.0.0'
        self.port = -1
        self.username = ''
        self.password = ''
    
    def setDBconfig(self, ip, port, username, password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
    
    def setUser(self, username, password):
        self.username = username
        self.password = password

    def setServer(self,ip, password):
        self.ip = ip
        self.password = password

    def connect(self):
        #self.db = MySQLdb.connect(self.ip, self.port, self.username, self.password)
        return self.db

    def close(self):
        pass
		#self.db.close()