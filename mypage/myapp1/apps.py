from django.apps import AppConfig
from django.http import HttpResponse


class Myapp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp1'

def index(request):
    return HttpResponse("This works!")
