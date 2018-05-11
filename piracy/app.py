from django_micro import configure, route, run
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Configure Django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'local.db',
    }
}
DEBUG = True
INSTALLED_APPS = ["django.contrib.staticfiles"]
MIDDLEWARE = ["middlewares.DummyAuthMiddleware"]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "OPTIONS": {
            "context_processors": ["context_processors.set_user"],
        },
    },
]
STATIC_URL = "/static/"
ALLOWED_HOSTS = ["*"]
configure(locals())


# Local Django classes
from .models import Pirate  # noqa: E402


# GET /favicon.ico
@route("favicon.ico", name="favicon")
def favicon(request):
    return HttpResponse("")


# GET /login : log in as username
@route("login", name="login")
def login(request):
    response = redirect("pirate_list")
    user = request.GET.get("user")
    if user:
        response.set_cookie("piracy_user", request.GET.get("user"))
    else:
        response.delete_cookie("piracy_user")
    return response


# GET / : list pirates
@route("", name="pirate_list")
class PirateList(ListView):
    model = Pirate


# GET /create : display create form
# POST /create : create pirate
@route("create", name="pirate_create")
class PirateCreate(CreateView):
    model = Pirate
    success_url = reverse_lazy("pirate_list")
    fields = ["name", "is_captain"]


# GET /update/:id : display update form
# POST /update/:id : update pirate
@route("update/<int:pk>", name="pirate_update")
class PirateUpdate(UpdateView):
    model = Pirate
    success_url = reverse_lazy("pirate_list")
    fields = ["name", "is_captain"]


# GET /delete/:id : display delete confirmation
# POST /delete/:id : delete pirate
@route("delete/<int:pk>", name="pirate_delete")
class PirateDelete(DeleteView):
    model = Pirate
    success_url = reverse_lazy("pirate_list")


# Run the app!
application = run()
