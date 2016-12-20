from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.categoria.forms import CategoriaForm
from apps.categoria.models import Categoria

# Create your views here.
def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
	return HttpResponse(lista, content_type='application/json')

def index_categoria(request):
	return render(request, 'categoria/index_categoria.html')


def categoria_view(request):
	if request.method== 'POST':
		form = CategoriaForm (request.POST)
		if form.is_valid():
			form.save()
		return redirect('categoria:index')

	else:
		form = CategoriaForm()

	return render(request, 'categoria/categoria_form.html', {'form':form})


def categoria_list(request):
	categoria = Categoria.objects.all().order_by('id_categoria')
	contexto = {'categoria':categoria}
	return render(request, 'categoria/categoria_list.html', contexto)




class CategoriaList(ListView):
	model = Categoria
	template_name = 'categoria/categoria_list.html'
	paginate_by = 2

class CategoriaCreate(CreateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'categoria/categoria_form.html'
	success_url = reverse_lazy('Categoria:categoria_listar')