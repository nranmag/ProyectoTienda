from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from .models import Producto

# Create your views here.

def tienda(request):
    productos=Producto.objects.all()
    page=request.GET.get('page', 1)
    try:
        paginator=Paginator(productos,12)
        productos=paginator.page(page)
    except:
        raise Http404

    return render(request, "tienda/tienda.html", {"productos":productos,"paginator":paginator})
