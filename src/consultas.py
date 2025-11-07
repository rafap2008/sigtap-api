from enum import Enum
from .fb import getSelect, getSelectColunas, getSelectCabecalho

class CabecalhoSql(Enum):
    SIM = "S"
    NAO = "N"
    UNICO = "U"

def getListaTabelas():
    return getSelect("SELECT TRIM(RDB$RELATION_NAME) AS TABELAS FROM RDB$RELATIONS WHERE RDB$SYSTEM_FLAG = 0")

def getColunasTabela(tabela, cabecalho=CabecalhoSql.UNICO):
    colunas = "TRIM(RDB$FIELD_NAME) COLUNA" if cabecalho == CabecalhoSql.NAO else "*"
    sql = f"SELECT {colunas} FROM RDB$RELATION_FIELDS WHERE RDB$RELATION_NAME = '{tabela.upper()}'"
    return getConsulta(sql, cabecalho)

def getDadosTabela(tabela, cabecalho=CabecalhoSql.UNICO):
    return getConsulta(f"SELECT * FROM {tabela}", cabecalho)

def getConsulta(script, cabecalho=CabecalhoSql.UNICO):
    match trataCabecalho(cabecalho):
        case CabecalhoSql.UNICO:
            return getSelectCabecalho(script)
        case CabecalhoSql.SIM:
            return getSelectColunas(script)
        case _:
            return getSelect(script)

def trataCabecalho(cabecalho):
    texto = str(cabecalho).upper()[0]
    
    if cabecalho == CabecalhoSql.SIM or texto == CabecalhoSql.SIM.value:
        return CabecalhoSql.SIM
    
    if cabecalho == CabecalhoSql.UNICO or texto == CabecalhoSql.UNICO.value:
        return CabecalhoSql.UNICO

    return CabecalhoSql.NAO

