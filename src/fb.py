import fdb

def getConexao():
    return fdb.connect(
        database        = "./data/sigtap.data",
        user            = "SYSDBA", 
        password        = "masterkey",
        charset         = "WIN1252",
        fb_library_name = "./data/fbclient.dll"
    )

def getCursor(conexao=None):
    if not conexao:
        conexao = getConexao()
    return conexao.cursor()

def getSelect(sql, conexao=None):
    cursor = getCursor(conexao)
    cursor.execute(sql)
    return cursor.fetchall()

