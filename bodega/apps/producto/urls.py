
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.producto.views import listadousuarios, index, producto_view, producto_list, producto_edit, \
	ProductoList, ProductoCreate, ProductoUpdate

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(ProductoCreate.as_view()), name='producto_crear'),
    url(r'^listar', login_required(ProductoList.as_view()), name='producto_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(ProductoUpdate.as_view()), name='producto_editar'),
    url(r'^listado', listadousuarios, name="listado"),
]
