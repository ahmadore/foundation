from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.index),
    url(r'^about/$', views.about),
    url(r'^contact/$', views.contact),
    url(r'^constitution/$', views.constitution),
    url(r'^apply/$', views.how_to_apply),
    url(r'^admin/', admin.site.urls),
    url(r'^events/', include('events.urls')),
]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)