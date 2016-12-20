from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.ingreso.forms import IngresoForm
from apps.ingreso.models import Ingreso

# Create your views here.
def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
	return HttpResponse(lista, content_type='application/json')

def index_ingreso(request):
	return render(request, 'ingreso/index_ingreso.html')


def ingreso_view(request):
	if request.method== 'POST':
		form = IngresoForm (request.POST)
		if form.is_valid():
			form.save()
		return redirect('ingreso:index')

	else:
		form = IngresoForm()

	return render(request, 'ingreso/ingreso_form.html', {'form':form})


def ingreso_list(request):
	ingreso = Ingreso.objects.all().order_by('id_ingreso')
	contexto = {'ingreso':ingreso}
	return render(request, 'ingreso/ingreso_list.html', contexto)




class IngresoList(ListView):
	model = Ingreso
	template_name = 'ingreso/ingreso_list.html'
	paginate_by = 2

class IngresoCreate(CreateView):
	model = Ingreso
	form_class = IngresoForm
	template_name = 'ingreso/ingreso_form.html'
	success_url = reverse_lazy('Ingreso:ingreso_listar')

