from django.urls import path
from . import views


app_name = 'publications'

urlpatterns = [
    path('list/', views.list_page, name='list'),


]
