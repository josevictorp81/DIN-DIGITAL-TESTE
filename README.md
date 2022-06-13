# DIN-DIGITAL-TESTE
Este é um [teste](https://github.com/dindigital/teste-back-end-2019) proposto pela [DIN DIGITAL](https://dindigital.io/) para desenvolvedores backend, na qual, deve ser feito uma miniAPI utilizando autenticação JWT e um CRUD para produtos, com as seguintes informações: nome, preço e peso.

## Requisitos
- [Docker](https://www.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Executar
Para executar a aplicação execute os seguintes comandos:

~ Cria a imagem para um container:
```
docker-compose build
```
~ Executar as migrations:
```
docker-compose run api python manage.py makemigrations
docker-compose run api python manage.py migrate
```
~ Crair superusuário:
```
docker-compose run api python manage.py createsuperuser
```
~ Executar os testes (opcional):
```
docker-compose run api python manage.py test
```
~ Executar o serviço/aplicação:
```
docker-compose up
```
~ Parar o serviço/aplicação:
```
docker-compose down
```

## Endpoints
Acesse `/docs` ou `/redoc` para ver a documentação dos endpoints.

## Frameworks e Bibliotecas
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/readme.html)