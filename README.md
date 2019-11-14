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
    * VUE_APP_URLAPI = 'http://endereco.com.br/api/tarefas/' **Url Da Api(Back-end)**
    * VUE_APP_VERSAOAPP = '1.0.0'  **Versão Da Aplicação**
* Back-end
    * ALLOWED_HOSTS='*' **Habilita quem pode acessar a aplicação**
    * DEBUG=True **Habilita a depuração do programa**
    * POSTGRESQL_DATABASE='Tarefas' **Nome do banco de dados**
    * POSTGRESQL_USER='User'**Nome de Usuario do banco de dados**
    * POSTGRESQL_PASSWORD='123' **Senha do do banco de dados**
    * POSTGRESQL_HOST='NomeDoServço' **Onde o bancode sera hospedado**
    * POSTGRESQL_PORT='5432' **Porta do banco de dados**
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
