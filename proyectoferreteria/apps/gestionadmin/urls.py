from django.urls import path
from proyectoferreteria.apps.gestionadmin.views import marca_index, marca_nueva, marca_edit, marca_delete, vista_principal
from proyectoferreteria.apps.gestionadmin.views import categoria_index, categoria_nueva, categoria_edit, categoria_delete
from proyectoferreteria.apps.gestionadmin.views import factura_index, factura_nueva, factura_edit, factura_delete
from proyectoferreteria.apps.gestionadmin.views import proveedor_index, proveedor_nueva, proveedor_edit, proveedor_delete
from proyectoferreteria.apps.gestionadmin.views import producto_index, producto_nueva, producto_edit, producto_delete
from proyectoferreteria.apps.gestionadmin.views import dash_index
from proyectoferreteria.apps.gestionadmin.views import ComprasView,compras,CompraDetDelete
from proyectoferreteria.apps.gestionadmin.views import probando

from .reportes import reporte_compras, reporte_comprasexcel, imprimir_compra
urlpatterns = [
    path('gestionadmin/vistaprincipal',vista_principal, name='Vista_principal'),
    
######### Marcas ###########     
    path('marca/index', marca_index, name='Marca_index'),
    path('marca/nueva', marca_nueva, name='Marca_crear'),
    path('marca/editar/<int:id_exp>/', marca_edit, name='Marca_editar'),
    path('marca/eliminar/<int:id_exp>/', marca_delete, name='Marca_delete'),

    path('admin/dash/index', dash_index, name='dash_index'),
######### Categorias ###########
    path('admin/categoria/index', categoria_index, name='Categoria_index'),
    path('categoria/nueva', categoria_nueva, name='Categoria_crear'),
    path('categoria/editar/<int:id_exp>/', categoria_edit, name='Categoria_editar'),
    path('categoria/eliminar/<int:id_exp>/', categoria_delete, name='Categoria_delete'),

######### Proveedor ###########     
    path('proveedor/index', proveedor_index, name='Proveedor_index'),
    path('proveedor/nueva', proveedor_nueva, name='Proveedor_crear'),
    path('proveedor/editar/<int:id_exp>/', proveedor_edit, name='Proveedor_editar'),
    path('proveedor/eliminar/<int:id_exp>/', proveedor_delete, name='Proveedor_delete'),

######### Factura ###########
    path('factura/index', factura_index, name='Factura_index'),
    path('factura/nueva', factura_nueva, name='Factura_crear'),
    path('factura/editar/<int:id_exp>/', factura_edit, name='Factura_editar'),
    path('factura/eliminar/<int:id_exp>/', factura_delete, name='Factura_delete'),
  

######### Producto ###########
    path('producto/index', producto_index, name='Producto_index'),
    path('producto/nueva', producto_nueva, name='Producto_crear'),
    path('producto/editar/<int:id_exp>/', producto_edit, name='Producto_editar'),
    path('producto/eliminar/<int:id_exp>/', producto_delete, name='Producto_delete'),

################################################################################################

    path('compras/',ComprasView.as_view(),name="compras_list"),
    path('compras/new',compras,name="compras_new"),
    path('compras/edit/<int:compra_id>/',compras,name="compras_edit"),
    path('compras/<int:compra_id>/delete/<int:pk>',CompraDetDelete.as_view(), name="compras_del"),
    path('compras/listado',reporte_compras,name="compras_print_all"),
    path('compras/<int:compra_id>/imprimir',imprimir_compra, name="compras_print_one"),

    path('compras/listadoexcell',reporte_comprasexcel,name="compras_print_all_excel"),

    path('admin/probando', probando, name='Categoria_index'),

]
