from django.conf.urls import url, include
from apps.categoria.views import index_categoria, CategoriaList, CategoriaCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', index_categoria, name=index_categoria),
	url(r'^categoria/listar$', login_required(CategoriaList.as_view()), name='categoria_listar'),
    url(r'^categoria/nueva$', login_required(CategoriaCreate.as_view()), name='categoria_crear'),
	

]