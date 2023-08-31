from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home" ),
    
    path('recetas/', recetas, name = "recetas"),
    path('update_receta/<id_receta>/', updateReceta, name="update_receta" ), 
    path('delete_receta/<id_receta>/', deleteReceta, name="delete_receta" ),
    path('create_receta/', createReceta, name="create_receta" ),
    path('detalle_receta/<int:id_receta>/', detalle_receta, name='detalle_receta'),
    
    
    path('clientes/', clientes, name = "clientes"),
    path('buscar_cliente/', buscarCliente, name ="buscar_cliente"),
    path('buscar2/', buscar2, name = "buscar2"),
    path('update_cliente/<id_cliente>/', updateCliente, name="update_cliente" ), 
    path('delete_cliente/<id_cliente>/', deleteCliente, name="delete_cliente" ),
    path('create_cliente/', createCliente, name="create_cliente" ),
    
    
    path('empleados/', EmpleadoList.as_view(), name="empleados" ),
    path('create_empleado/', EmpleadoCreate.as_view(), name="create_empleado" ),    
    path('update_empleado/<int:pk>/', EmpleadoUpdate.as_view(), name="update_empleado" ),
    path('delete_empleado/<int:pk>/', EmpleadoDelete.as_view(), name="delete_empleado" ),
    
    
    path('proveedores/', ProveedorList.as_view(), name="proveedores" ),
    path('create_proveedor/', ProveedorCreate.as_view(), name="create_proveedor" ),    
    path('update_proveedor/<int:pk>/', ProveedorUpdate.as_view(), name="update_proveedor" ),
    path('delete_proveedor/<int:pk>/', ProveedorDelete.as_view(), name="delete_proveedor" ),
    
    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ), 
    
    path('acerca_de_mi/', acerca_de_mi, name='acerca_de_mi')
]
