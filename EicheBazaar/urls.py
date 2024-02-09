from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainshop.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'mainshop.views.handler404'
handler505 = 'mainshop.views.handler505'
handler403 = 'mainshop.views.handler403'