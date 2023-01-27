# desafio-backend


<a name="install"></a>

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
