import fdb
import json

def getConexao():
    return fdb.connect(
        database        = "./data/SISAIH00.GDB",
        user            = "SYSDBA", 
        password        = "masterkey",
        #charset         = "WIN1252",
        fb_library_name = "./fb/fbclient.dll"
    )

def getCursor(conexao=None):
    if not conexao:
        conexao = getConexao()
    return conexao.cursor()

def getSelect(sql, conexao=None):
    try:
        cursor = getCursor(conexao)
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    except fdb.Error as e:
        return f"Falha ao efetuar consulta: {e}"

    except Exception as e:
        return f"Falha ao efetuar consulta: {e}"
    
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def getSelectColunas(sql, conexao=None):
    try:
        cursor = getCursor(conexao)
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))

        return results
        #json_output = json.dumps(results, indent=2)
        #return json_output
    except fdb.Error as e:
        return f"Falha ao efetuar consulta: {e}"

    except Exception as e:
        return f"Falha ao efetuar consulta: {e}"

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def getSelectCabecalho(sql, conexao=None):
    try:
        cursor = getCursor(conexao)
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        rows.insert(0, columns)
        return rows
    except fdb.Error as e:
        return f"Falha ao efetuar consulta: {e}"

    except Exception as e:
        return f"Falha ao efetuar consulta: {e}"

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()