from django.urls import path
from . import views

app_name = 'basic_app'

#using the as_view() is a much better methond instead of the views.index etc
urlpatterns = [
    path('', views.SchoolListView.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),

    #path('', views.IndexView.as_view(),name='index'),
    # what the instructor wrote:
    # url(r'^(?<pk>[-\W]+))/$',views.SchoolDetailView.as_view())
    #the line below did not work as School is wrong
    #path('School/<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
    # the below code worked as it asked for the number of the pk.
]
