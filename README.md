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
January 04, 2023 - 13:53:34
Django version 4.1.5, using settings 'djangoAnimes.settings'
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
        "tipo": "3",
        "data": "2019-03-01",
        "valor": "142.00",
        "cpf": "09620676017",
        "cartao": "4753****3153",
        "hora": "15:34:53",
        "dono_da_loja": "JOÃO MACEDO   ",
        "nome_loja": "BAR DO JOÃO",
        "total_loja": 812.0,
        "total_transacoes": 6
    }, 
    {
        "tipo": "5",
        "data": "2019-03-01",
        "valor": "132.00",
        "cpf": "55641815063",
        "cartao": "3123****7687",
        "hora": "14:56:07",
        "dono_da_loja": "MARIA JOSEFINA",
        "nome_loja": "LOJA DO Ó - MATRIZ",
        "total_loja": 868.0,
        "total_transacoes": 6
    },
    {
        "tipo": "3",
        "data": "2019-03-01",
        "valor": "122.00",
        "cpf": "84515254073",
        "cartao": "6777****1313",
        "hora": "17:27:12",
        "dono_da_loja": "MARCOS PEREIRA",
        "nome_loja": "MERCADO DA AVENIDA",
        "total_loja": 4670.4,
        "total_transacoes": 16
    },
 ]

 Rota /api/file/<Nome_Da_Loja>/
 Retorno:
 [
    {
        "tipo": "3",
        "data": "2019-03-01",
        "valor": "142.00",
        "cpf": "09620676017",
        "cartao": "4753****3153",
        "hora": "15:34:53",
        "dono_da_loja": "JOÃO MACEDO   ",
        "nome_loja": "BAR DO JOÃO",
        "total_loja": 812.0,
        "total_transacoes": 6
    },
    {
      "tipo": "2",
      "data": "2019-03-01",
      "valor": "112.00",
      "cpf": "09620676017",
      "cartao": "3648****0099",
      "hora": "23:42:34",
      "dono_da_loja": "JOÃO MACEDO   ",
      "nome_loja": "BAR DO JOÃO",
      "total_loja": 812.0,
      "total_transacoes": 6
  }
]
```
