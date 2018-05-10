Django Partial Forms Example
============================

This repository demonstrates some pitfalls when using "partial" forms
in Django, e.g. when some fields are conditionnally hidden depending
on context.


Setup
-----

NB: This repository has been tested with CPython 3.6.x. We're unsure
of the compatibility with other python versions. You might want to
use [pyenv](https://github.com/pyenv/pyenv) for switching between
python versions.

Install dependencies:
```
# Optional:
# virtualenv -p python3 ~/.virtualenvs/django-partial-forms-example
# source ~/.virtualenvs/django-partial-forms-example/bin/activate
pip install -r requirements.txt
```

Start the server:
```
cd piracy/
python app.py runserver 127.1:8765
```

Open the app:
```
open http://localhost:8765
```
