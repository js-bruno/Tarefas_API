# Aplicação - Lista de Tarefas

## Pré-Requisitos

* python 3.6.9 
* django 2.2.4
* @vue/cli 4.0.5
* django-cors-headers 3.1.1 
* psycopg2 2.7.3
* psycopg2-binary 2.7.4
* djangorestframework 3.10.2
* nodejs 10.13.0

### Desenvolvido com

 * VueJS - Framework JS

### Variáveis da aplicação

* VUE_APP_URLAPI = URL da API
* STATIC_ROOT = pasta na qual os arquivos estáticos serão armazenados
* STATICFILES_DIRS = lista de pastas em que o Django procurará arquivos estáticos adicionais além da pasta static
* CORS_ORIGIN_ALLOW_ALL = bloqueia o cors 
* STATIC_URL = local da pasta estática
* ALLOWED_HOSTS =  habilita quem pode acessar a aplicação

### Desenvolvido por

* GeoMK Desenvolvimento de Programas De Computador
* Estagiários da equipe de desenvolvimento

### Comandos da aplicação
```
npm run serve -- --{{MYPORT}}  
python manage.py runserver {{MYPORT}}
```