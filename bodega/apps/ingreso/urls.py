from django.conf.urls import url, include
from apps.ingreso.views import index_ingreso, IngresoList, IngresoCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', index_ingreso, name=index_ingreso),
	url(r'^ingreso/listar$', login_required(IngresoList.as_view()), name='ingreso_listar'),
    url(r'^ingreso/nueva$', login_required(IngresoCreate.as_view()), name='ingreso_crear'),
	

]