from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, kwargs={"name": "Вагизова Аделина Ильдаровна", "age": 18, "interes": "программирование"}),
    re_path('about', views.about),
    re_path('contacts', views.contacts),
]
