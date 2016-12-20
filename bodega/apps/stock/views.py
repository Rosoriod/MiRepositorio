from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.stock.forms import StockForm
from apps.stock.models import Stock

# Create your views here.
def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['username', 'first_name'])
	return HttpResponse(lista, content_type='application/json')

def index_stock(request):
	return render(request, 'ingreso/index_ingreso.html')

def stock_list(request):
	stock = Stock.objects.all().order_by('id_stock')
	contexto = {'stock':stock}
	return render(request, 'stock/stock_list.html', contexto)


class StockList(ListView):
	model = Stock
	template_name = 'stock/stock_list.html'
	paginate_by = 2
