from django.urls import path
from . import views


app_name = 'resources'

urlpatterns = [
    path('list/', views.list_page, name='list'),
    path('detail/<int:item_id>', views.detail_page, name='detail'),

]
