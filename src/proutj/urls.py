
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home_page, about_page, subscription_page


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('subscription/', subscription_page, name='subscription'),
    path('', include('edits.urls', namespace='edits')),
    path('archives/', include('archives.urls', namespace='archives')),
    path('resources/', include('resources.urls', namespace='resources')),
    path('publications/', include('publications.urls', namespace='publications')),
    path('downloads/', include('downloads.urls', namespace='downloads')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
