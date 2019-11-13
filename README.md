# Aplicação - Lista de Tarefas

## Pré-Requisitos

* python 3.6.9 
* django 2.2.4
* django-cors-headers 3.1.1 
* psycopg2 2.7.3
* psycopg2-binary 2.7.4
* djangorestframework 3.10.2
* nodejs 10.13.0

### Desenvolvido com

 * VueJS - Framework JS

### Variáveis da aplicação

* Front-end
    * VUE_APP_URLAPI = URL da API(http://endereco.com.br:{{MYPORT}}/api/tarefas/)
    * VUE_APP_VERSAOAPP = Versão da aplicação 
* Back-end
    * ALLOWED_HOSTS =  Habilita quem pode acessar a aplicação
    * DEBUG = Depuração da aplicação
    * POSTGRESQL_DATABASE = Nome do banco de dados
    * POSTGRESQL_USER = Nome de Usuario do banco de dados
    * POSTGRESQL_PASSWORD = Senha do do banco de dados
    * POSTGRESQL_HOST = Host do banco de dados
    * POSTGRESQL_PORT = Porta do banco de dados
### Desenvolvido por

* GeoMK Desenvolvimento de Programas De Computador
* Estagiários da equipe de desenvolvimento

### Comandos para subir as aplicações
```
* Front-End
npm run serve -- --port 0.0.0.0:8080
* Back-End
python manage.py runserver 0.0.0.0:8000
```
