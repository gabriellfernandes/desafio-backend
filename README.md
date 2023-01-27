# desafio-backend

## 1. Sobre

Sistema de upload de arquivos CNABA que comverte para um arquivo json e exibe na tela todos os dados.


## 2. Instalação e uso

### 2.1 Requisitos

- Python a partir da versão 3.11.1
- Gerenciador de pacotes pip
- Banco de dados PostgreSQL

### 2.2 Instalação

 2.2.1 - Crie um banco de dados chamado Django_animes_database no PostgreSQL
 2.2.2 - Após o clone no repositório crie um ambiente de desenvolvimento:
 ```
 python -m venv venv
 ```
 
 2.2.3 - Após a criação do ambiente virtual voce terá que ativa-lo com o seguinte comando
 
 para linux:
 ```
 source/venv/bin/activate
 ```
 
 para windows:
 ```
 .\venv\Scripts\activate
 ```
 
2.2.4 - Agora que ja ativou o ambiênte de desenvolvimento voce terá que instalar as dependências do projeto
```
pip install -r requirements.txt
```

2.2.5 - Após instalar as dependências vamos persistir as migrations no banco de dados
```
python manage.py migrate
```

2.2.6 - Para rodar projeto utilize o comando 
```
python manage.py runserver
``` 

2.2.7 - Caso de tudo certo receberá uma mensagem parecida com essa:

```
System check identified no issues (0 silenced).
January 27, 2023 - 15:40:40
Django version 4.1.5, using settings 'desafio_backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## 3 Rotas
```
3.1 - Rota: /api/ - html template com a opção de upload de arquivos text do padrão CNBA

```
```

3.2 - Rota: /api/file/ - get all de todas a Lojas e Transações

```
```
3.3 - rota: /api/file/<Nome_Da_Loja> - get que utiliza o nome da loja como filtro para mostras as Transações da loja

```
## 4 Retorno

```
 Rota /api/file/
 Retorno:
 [
    {
        "data": "2019-03-01",
        "cpf": "09620676017",
        "cartao": "4753****3153",
        "hora": "15:34:53",
        "dono_da_loja": "JOÃO MACEDO   ",
        "nome_loja": "BAR DO JOÃO",
        "total_da_loja": -204.0,
        "total_transacoes": 6,
        "tipo_da_transacao": "Financiamento",
        "valor_da_transacao": -142.0
    },
    {
        "data": "2019-03-01",
        "cpf": "55641815063",
        "cartao": "3123****7687",
        "hora": "14:56:07",
        "dono_da_loja": "MARIA JOSEFINA",
        "nome_loja": "LOJA DO Ó - MATRIZ",
        "total_da_loja": 460.0,
        "total_transacoes": 6,
        "tipo_da_transacao": "Recibimento Empréstimo",
        "valor_da_transacao": 132.0
    },
    {
        "data": "2019-03-01",
        "cpf": "84515254073",
        "cartao": "6777****1313",
        "hora": "17:27:12",
        "dono_da_loja": "MARCOS PEREIRA",
        "nome_loja": "MERCADO DA AVENIDA",
        "total_da_loja": 978.4,
        "total_transacoes": 16,
        "tipo_da_transacao": "Financiamento",
        "valor_da_transacao": -122.0
    }
 ]
```
```
Rota /api/file/LOJA DO Ó - MATRIZ/
 Retorno:
 [
     {
        "data": "2019-03-01",
        "cpf": "55641815063",
        "cartao": "3123****7687",
        "hora": "14:56:07",
        "dono_da_loja": "MARIA JOSEFINA",
        "nome_loja": "LOJA DO Ó - MATRIZ",
        "total_da_loja": 460.0,
        "total_transacoes": 6,
        "tipo_da_transacao": "Recibimento Empréstimo",
        "valor_da_transacao": 132.0
    },
    {
        "data": "2019-03-01",
        "cpf": "55641815063",
        "cartao": "1234****3324",
        "hora": "09:00:02",
        "dono_da_loja": "MARIA JOSEFINA",
        "nome_loja": "LOJA DO Ó - MATRIZ",
        "total_da_loja": 460.0,
        "total_transacoes": 6,
        "tipo_da_transacao": "Debito",
        "valor_da_transacao": 200.0
    }
]
```
