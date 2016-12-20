from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.producto.forms import ProductoForm
from apps.producto.models import Producto

# Create your views here.
def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
	return HttpResponse(lista, content_type='application/json')

def index(request):
	return render(request, 'producto/index.html')


def producto_view(request):
	if request.method== 'POST':
		form = ProductoForm (request.POST)
		if form.is_valid():
			form.save()
		return redirect('producto:index')

	else:
		form = ProductoForm()

	return render(request, 'producto/producto_form.html', {'form':form})


def producto_list(request):
	producto = Producto.objects.all().order_by('id_producto')
	contexto = {'producto':producto}
	return render(request, 'producto/producto_list.html', contexto)

def producto_edit(request, id_producto):
	producto = Producto.objects.get(id=id_producto)
	if request.method == 'GET':
		form = ProductoForm(instance=producto)
	else:
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
		return redirect('producto:producto_listar')
	return render(request, 'producto/producto_form.html', {'form':form})


class ProductoList(ListView):
	model = Producto
	template_name = 'producto/producto_list.html'
	paginate_by = 2

class ProductoCreate(CreateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'producto/producto_form.html'
	success_url = reverse_lazy('producto:producto_listar')

class ProductoUpdate(UpdateView):
	model = Producto
	form_class = ProductoForm
	template_name = 'producto/producto_form.html'
	success_url = reverse_lazy('producto:producto_listar')
	