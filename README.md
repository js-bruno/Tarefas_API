# Aplicação - Lista de Tarefas

## Pré-Requisitos

* python 3.6.9 
* django 2.2.4
* django-cors-headers 3.1.1 
* psycopg2 2.7.3
* psycopg2-binary 2.7.4
* djangorestframework 3.10.2
* nodejs 10.13.0
* postgress 9.6
* nginx 1.14.2
* pgadmin imagedpage/pgadmin4

### Desenvolvido com

 * VueJS - Framework JS

### Envs da aplicação

* Front-end
    * VUE_APP_URLAPI=/api/tarefas/
    * VUE_APP_VERSAOAPP=1.0.0
* Back-end
    * ALLOWED_HOSTS=*
    * DEBUG=True 
    * POSTGRESQL_DATABASE=tarefas
    * POSTGRESQL_USER=User
    * POSTGRESQL_PASSWORD=e^$gofA!Z%6@
    * POSTGRESQL_HOST=nomedoservico
    * POSTGRESQL_PORT=5432

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

### Informações adicionais
* Usar pgadmin4 para criação do banco ou criação de script para a criação do mesmo.
* O endpoint da api(VUE_APP_URLAPI) deve ser apontada pelo nginx.
* Apos subir o back-end deve ser executado o comando de migrate.

```
    python manage.py migrate
```
* Não colocar endereço no nginx, vue não está aceitando.