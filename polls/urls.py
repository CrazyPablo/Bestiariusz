from django.urls import path

from . import views

#app_name = "polls"
urlpatterns = [
path("strzyga/", views.strzyga, name="strzyga"),
path("", views.index, name="index"),
]
