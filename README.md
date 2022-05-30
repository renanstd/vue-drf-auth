# vue-drf-auth

[![Python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/JWT-black?style=flat&logo=JSON%20web%20tokens)](https://jwt.io/)
[![Insomnia](https://img.shields.io/badge/Insomnia-black?style=flat&logo=insomnia&logoColor=5849BE)](https://insomnia.rest/)

## Descrição

Apenas um minúsculo estudo sobre autenticação via token JWT usando um backend Django e um frontend VUE.

## Subindo os serviços

### Backend

[Poetry](https://python-poetry.org/) reqired.

```sh
cd backend/backend_api
```

```sh
poetry install
```

```sh
poetry run python manage.py migrate
```

```sh
poetry run python manage.py rnserver
```

### Frontend

```sh
cd frontend/front-todo
```

```sh
npm run serve
```

## Screenshots

![Login form](images/login_form.png)

![TODO list](images/list.png)
