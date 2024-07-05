from django.urls import path, include

from ProyectoTiendaApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="Home"),
    path('servicios', include('servicios.urls')),
    path('blog', include('blog.urls')),
    path('contacto', include('contacto.urls')),
    path('tienda', include('tienda.urls')),
    path('carro', include('carro.urls')),
    path('pedidos', include('pedidos.urls')),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)