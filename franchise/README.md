## Este projeto foi feito com:

* [Python 3.10.2](https://www.python.org/)
* [Django 3.2.11](https://www.djangoproject.com/)
* [Django Rest Framework 3.13.1](https://www.django-rest-framework.org/)

## Como rodar o projeto?

* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
cd franchise
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

A aplicação estará rodando na porta 8000.