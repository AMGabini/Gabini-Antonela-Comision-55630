#_____IMPORTACIONES_____#
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#_____FUNCION_HOME_____#
def home(request):
    return render(request, "aplicacion/home.html")



#_____FUNCIONES_DE_RECETAS:_Implementacion_CRUD_____#

@login_required
def recetas(request):
    contexto = {'Receta': Receta.objects.all()}
    return render(request, "aplicacion/recetas.html", contexto)

@login_required
def updateReceta(request, id_receta):
    receta = Receta.objects.get(id=id_receta)
    if request.method == "POST":
        miForm = RecetaForm(request.POST)
        if miForm.is_valid():
            receta.titulo = miForm.cleaned_data.get('titulo') 
            receta.ingredientes = miForm.cleaned_data.get('ingredientes')
            receta.instrucciones = miForm.cleaned_data.get('instrucciones')
            receta.tiempo_preparacion = miForm.cleaned_data.get('tiempo_preparacion') 
            receta.save()
            return redirect(reverse_lazy('recetas'))   
    else:
        miForm = RecetaForm(initial={
            'titulo': receta.titulo,
            'ingredientes': receta.ingredientes,
            'instrucciones': receta.instrucciones,
            'tiempo_preparacion': receta.tiempo_preparacion,
        })
    return render(request, "aplicacion/recetaForm.html", {'form': miForm})

@login_required
def deleteReceta(request, id_receta):
    receta = Receta.objects.get(id=id_receta)
    receta.delete()
    return redirect(reverse_lazy('recetas'))

@login_required
def createReceta(request):    
    if request.method == "POST":
        miForm = RecetaForm(request.POST)
        if miForm.is_valid():
            r_titulo = miForm.cleaned_data.get('titulo')
            r_ingredientes = miForm.cleaned_data.get('ingredientes')
            r_instrucciones = miForm.cleaned_data.get('instrucciones')
            r_tiempo_preparacion = miForm.cleaned_data.get('tiempo_preparacion')
            receta = Receta(titulo=r_titulo, 
                            ingredientes=r_ingredientes,
                            instrucciones=r_instrucciones,
                            tiempo_preparacion=r_tiempo_preparacion,
                            )
            receta.save()
            return redirect(reverse_lazy('recetas'))
    else:
        miForm = RecetaForm()

    return render(request, "aplicacion/recetaForm.html", {"form":miForm})

@login_required
def detalle_receta(request, id_receta):
    receta = Receta.objects.get(id=id_receta)
    contexto = {'receta': receta}
    return render(request, "aplicacion/detalle_receta.html", contexto)

#_____FUNCIONES_DE_CLIENTE:_Implementacion_CRUD_____#

@login_required
def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "aplicacion/clientes.html", contexto)

@login_required
def buscarCliente(request):
    return render(request, "aplicacion/buscarCliente.html")

@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        cliente = Cliente.objects.filter(nombre__icontains=patron)
        contexto = {'clientes': cliente} 
        return render(request, "aplicacion/clientes.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

@login_required
def updateCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get('nombre')
            cliente.apellido = miForm.cleaned_data.get('apellido')  
            cliente.email = miForm.cleaned_data.get('email')
            cliente.telefono = miForm.cleaned_data.get('telefono')
            cliente.direccion = miForm.cleaned_data.get('direccion') 
            cliente.save()
            return redirect(reverse_lazy('clientes'))   
    else:
        miForm = ClienteForm(initial={
            'nombre': cliente.nombre,
            'apellido' : cliente.apellido,
            'email': cliente.email,
            'telefono': cliente.telefono,
            'direccion': cliente.direccion,
        })
    return render(request, "aplicacion/clienteForm.html", {'form': miForm})

@login_required
def deleteCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect(reverse_lazy('clientes'))

@login_required
def createCliente(request):    
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            c_nombre = miForm.cleaned_data.get('nombre')
            c_apellido = miForm.cleaned_data.get('apellido')
            c_email = miForm.cleaned_data.get('email')
            c_telefono = miForm.cleaned_data.get('telefono')
            c_direccion = miForm.cleaned_data.get('direccion')
            cliente = Cliente(nombre=c_nombre, 
                              apellido=c_apellido,
                              email=c_email,
                              telefono=c_telefono,
                              direccion=c_direccion,
                             )
            cliente.save()
            return redirect(reverse_lazy('clientes'))
    else:
        miForm = ClienteForm()

    return render(request, "aplicacion/clienteForm.html", {"form":miForm})



#_____FUNCIONES_DE_EMPLEADO:_Implementacion_CBV_____#

class EmpleadoList(LoginRequiredMixin, ListView):
    model = Empleado

class EmpleadoCreate(LoginRequiredMixin, CreateView):
    model = Empleado
    fields = ['nombre','apellido', 'puesto', 'salario', 'fecha_contratacion']
    success_url = reverse_lazy('empleados')

class EmpleadoUpdate(LoginRequiredMixin, UpdateView):
    model = Empleado
    fields = ['nombre','apellido', 'puesto', 'salario', 'fecha_contratacion']
    success_url = reverse_lazy('empleados')

class EmpleadoDelete(LoginRequiredMixin, DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')


#_____FUNCIONES_DE_PROVEEDORES:_Implementacion_CBV_____#

class ProveedorList(LoginRequiredMixin, ListView):
    model = Proveedor

class ProveedorCreate(LoginRequiredMixin, CreateView):
    model = Proveedor
    fields = ['nombre_empresa','contacto', 'email', 'telefono', 'direccion']
    success_url = reverse_lazy('proveedores')

class ProveedorUpdate(LoginRequiredMixin, UpdateView):
    model = Proveedor
    fields = ['nombre_empresa','contacto', 'email', 'telefono', 'direccion']
    success_url = reverse_lazy('proveedores')

class ProveedorDelete(LoginRequiredMixin, DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedores')


#_____FUNCIONES_DE_LOGUIN/LOGOUT/REGISTRACION_____#

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm})    

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/base.html")
        else:
            return render(request,"aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })

#_____FUNCION_ACERCA_DE_MI_____#

def acerca_de_mi(request):
    return render(request, 'aplicacion/acerca_de_mi.html')