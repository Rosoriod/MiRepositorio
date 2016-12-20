from django.conf.urls import url, include

from apps.stock.views import index_stock, StockList
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', index_stock, name=index_stock),
	url(r'^stock/listar$', login_required(StockList.as_view()), name='stock_listar'),
    
	

]