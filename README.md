# sigtap-api

## Este é um serviço API para disponibilizar consultas na base de dados do SIGTAP.


### Seguem as rotas disponíveis:

* /
* /rotas
* /lista-tabelas
* /colunas-tabela/<-tabela->/<-cabecalho->
* /colunas-tabela/<-tabela->
* /dados-tabela/<-tabela->/<-cabecalho->
* /dados-tabela/<-tabela->
* /consulta/<-script->/<-cabecalho->
* /consulta/<-script->

## Observação 1

As rotas informadas acima são exemplo, e podem estar desatualizadas.
\
Para verificar todas a rotas corretamente, deve-se executar o serviço e acessar a rota printipal (/)

## Observação 2

### Para as APIs que possuem o parâmetro "cabecalho", pode-se informar:

* "U" = "Único" - Para retornar o cabeçalho em um registro, e os dados nos demais registros (simulando uma planilha).
\
Exemplo:
\
```
[
  [
    "Nome",
    "Pais"
  ],
  [
    "Rafael Pinheiro",
    "Brasil"
  ],
  [
    "Maria",
    "Itália"
  ]
]
```
* "S" = "Sim" - Para retornar o os nomes das colunas junto dos valores (padrão de um arquivo JSON).
\
Exemplo:
\
```
[
  [
    "Nome": "Rafael Pinheiro",
    "Pais": "Brasil"
  ],
  [
    "Nome": "Maria",
    "Pais": "Itália"
  ]
]
```
* "N" = "Não" - Para retornar apenas os dados, sem os nomes da colunas.
\
Exemplo:
\
```
[
  [
    "Rafael Pinheiro",
    "Brasil"
  ],
  [
    "Maria",
    "Itália"
  ]
]
```
* Ao não informar, o padrão será o modo "Único"

