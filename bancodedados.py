from mysql.connector import connect

def abredb(self,host,banco,senha,usuario):
    return connect(host=host, database=banco, user=usuario, password=senha)
def fechadb(self,con):
    return con.close()
