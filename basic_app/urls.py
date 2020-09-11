from django.urls import path
from . import views

app_name = 'basic_app'

#using the as_view() is a much better methond instead of the views.index etc
urlpatterns = [
    path('', views.IndexView.as_view()),
]
