from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.main.urls', namespace='main')),
    url(r'^', include('apps.users.urls', namespace='users')),
    url(r'^', include('apps.inventario.urls', namespace='inventario')),
    # url(r'^', include('apps.products.urls', namespace='products')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT,}
        ),
    ]
