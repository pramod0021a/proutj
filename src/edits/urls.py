from django.urls import path
from . import views


app_name = 'edits'

urlpatterns = [
    path('', views.index, name='home'),
    path('detail1/<int:id_1>', views.details1, name='detail1'),
    path('detail2/<int:id_2>', views.details2, name='detail2'),
    path('detail3/<int:id_3>', views.details3, name='detail3'),
    path('detail4/<int:id_4>', views.details4, name='detail4'),
    path('detail5/<int:id_5>', views.details5, name='detail5'),
    path('detail6/<int:id_6>', views.details6, name='detail6'),
    path('editorial/<int:id_edit>', views.editorial, name='editorial'),
    path('coverstory/<int:id_story>', views.coverstory, name='coverstory'),

    path('contact/', views.contact_page, name='contact'),
    # path('about/', views.about_page, name='about'),
]
