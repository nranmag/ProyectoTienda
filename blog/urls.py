from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blog/',views.blog, name="Blog"),
    path('blog/categoria/<int:categoria_id>/',views.categoria, name="categoria")
]