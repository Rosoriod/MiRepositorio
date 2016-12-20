from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.salida.forms import SalidaForm
from apps.salida.models import Salida

# Create your views here.
def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
	return HttpResponse(lista, content_type='application/json')

def index_salida(request):
	return render(request, 'salida/index_salida.html')


def salida_view(request):
	if request.method== 'POST':
		form = SalidaForm (request.POST)
		if form.is_valid():
			form.save()
		return redirect('salida:index')

	else:
		form = SalidaForm()

	return render(request, 'salida/salida_form.html', {'form':form})


def salida_list(request):
	salida = Salida.objects.all().order_by('id_salida')
	contexto = {'salida':salida}
	return render(request, 'salida/salida_list.html', contexto)




class SalidaList(ListView):
	model = Salida
	template_name = 'salida/salida_list.html'
	paginate_by = 2

class SalidaCreate(CreateView):
	model = Salida
	form_class = SalidaForm
	template_name = 'salida/salida_form.html'
	success_url = reverse_lazy('Salida:salida_listar')