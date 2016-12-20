from django.conf.urls import url, include
from apps.salida.views import index_salida, SalidaList, SalidaCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', index_salida, name=index_salida),
	url(r'^salida/listar$', login_required(SalidaList.as_view()), name='salida_listar'),
    url(r'^salida/nueva$', login_required(SalidaCreate.as_view()), name='salida_crear'),
	

]