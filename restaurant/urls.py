from django.urls import path, include
from . import views


urlpatterns = [
    # path("", views.sayHello, name="sayHello"),
    path("", views.index, name="index"),
]
