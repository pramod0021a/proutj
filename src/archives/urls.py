from django.urls import path
from . import views


app_name = 'archives'

urlpatterns = [
    path('list/', views.list_page, name='list'),
    path('detail/<int:mag_id>', views.detail_page, name='detail'),

]
