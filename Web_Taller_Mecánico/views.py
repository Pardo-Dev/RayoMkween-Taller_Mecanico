from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login as login_aut
from .models import Mecanico, Especialidad, regAte, Producto, Galeria
from django.contrib.auth.decorators import login_required,permission_required
from .Carrito import *


# Create your views here.
def index(request):
    especialidades = Especialidad.objects.all()
    atenciones = regAte.objects.filter(publicar=True).order_by("-idAtencion")[:3]
    contexto = {
        "especialidades" : especialidades,
        "atenciones": atenciones
    }
    return render(request, 'index.html', contexto)

def mecanicos(request):
    mecanicos = Mecanico.objects.all()
    contexto = {
        "mecanicos":mecanicos
    }
    return render(request, 'mecanicos.html', contexto)

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje enviado correctamente!")
            return redirect(to="INDEX")
        else:
            data["form"] = formulario
    return render(request, 'contacto.html', data)

def producto(request):
    productos = Producto.objects.all()
    contexto = {
        "productos": productos
    }
    return render(request, 'productos.html', contexto)

def login(request):
    if request.POST:
        nom=request.POST.get("txtNombre")
        con=request.POST.get("pwdPass1")
        usu= authenticate(request,username=nom,password=con)
        if usu is not None and usu.is_active:
            login_aut(request,usu)

            return redirect(to="INDEX")
    contexto={'mensaje':'Usuario/Contraseña Incorrecto'}   
    
    return render(request, 'login.html', contexto)

def cerrar_sesion(request):
    logout(request)
    return redirect(to="INDEX")

def registro(request):
    contexto={'mensaje':'noooo'}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email= request.POST.get("txtCorreo")
        password= request.POST.get("pwd1")
        passwordConf = request.POST.get("pwd2")
        usu = User()
        usu.set_password(password)
        usu.email=email
        usu.username=nombre
        usu.last_name=apellido
        usu.first_name=nombre
        try:
            if password == passwordConf:
                usu.save()
                messages.success(request, "Ha sido registrado correctamente!")
                return redirect(to="LOGIN")
            else:
                
                messages.error(request, "Pone la weaaaa igual oe")
        except:
            contexto['mensaje']='error al grabar'    
    return render(request,"registro.html",contexto)

def galeria(request):
    atenciones = regAte.objects.all()
    contexto = {
        "atenciones": atenciones
    }
    return render(request, 'galeria.html', contexto)


@login_required(login_url='/login/')
@permission_required('auth.add_user',login_url='/login/')
def registrar_atencion(request):
    mecanico = Mecanico.objects.all()
    especialidad = Especialidad.objects.all()
    contexto = {
        "especialidades": especialidad,
        "mecanicos":mecanico
    }

    if request.POST:
        atencion = regAte()

        tipo_atencion = request.POST.get("cboEspecialidad")
        encargado = request.POST.get("cboMecanico")
        titulo = request.POST.get("txtTitulo")
        descripcion = request.POST.get('txtDescripcion')
        materiales = request.POST.get('txtMateriales')
        fecha = request.POST.get('datFecha')
        foto = request.FILES.get('fileFoto')
        if foto is not None:
            atencion.foto = foto
        
            atencion.tipoAte = Especialidad.objects.get(id = int(tipo_atencion))
            atencion.rutMeca = Mecanico.objects.get(rut = int(encargado))
            atencion.titulo=titulo 
            atencion.descAte=descripcion
            atencion.materiales =materiales 
            atencion.fecha= fecha
            
            atencion.save()
            messages.success(request, "Atencion registrada correctamente!")

            return redirect(to="INDEX")
    return render(request, 'registrar_atencion.html',contexto)

def filtro_nombre(request):
    mecanicos = Mecanico.objects.all()
    if request.POST:
        nomMec = request.POST.get("txtBuscar")
        mecanicos = Mecanico.objects.filter(nombre=nomMec)
    contexto = {'mecanicos':mecanicos}
    return render(request, "mecanicos.html", contexto)

def filtro_espe(request):
    espe = request.POST.get("cboEspecialidad")
    especialidades = Especialidad.objects.all()
    if espe=='Todas':
        mec= Mecanico.objects.all()
        contar = Mecanico.objects.all().count()
    else:
        obj_espe = Especialidad.objects.get(nombre=espe)
        mec = Mecanico.objects.filter(especialidad=obj_espe)
        contar = Mecanico.objects.filter(especialidad=obj_espe).count()
    
    contexto={'mecanicos':mec,'cantidad':contar,'especialidades':especialidades}
    return render(request,"mecanicos.html",contexto)

def perfil(request):
    return render(request, 'perfil.html')


# Carrito funciones
@login_required(login_url='/login/')
def agregar_carrito(request, id_producto):
    carrito = Carrito(request)
    produ = Producto.objects.get(idProducto = id_producto)
    carrito.agregar(produ)
    return redirect('PRODUCTOS')

def restar_carrito(request, id_producto):
    carrito = Carrito(request)
    produ = Producto.objects.get(idProducto = id_producto)
    carrito.restar(produ)
    return redirect('PRODUCTOS')

def eliminar_carrito(request, id_producto):
    carrito = Carrito(request)
    produ = Producto.objects.get(idProducto = id_producto)
    carrito.eliminar(produ)
    return redirect('PRODUCTOS')

def vaciar(request):
    carrito = Carrito(request)
    carrito.vaciar()
    return redirect('PRODUCTOS')


@login_required(login_url='/login/')
def ficha(request, id_atencion):
    atencion = regAte.objects.get(idAtencion= id_atencion)
    galeria = Galeria.objects.filter(atencion = atencion)
    contexto = {"atenciones": atencion, "galerias":galeria}

    return render(request, 'ficha.html', contexto)


@login_required(login_url='/login/')
@permission_required('auth.delete_reg',login_url='/login/')
def eliminar(request, id_atencion):
    atencion = regAte.objects.get(idAtencion = id_atencion)
    contexto = {"atenciones" : atencion}
    try:
        atencion.delete()
        print('Elimino')
        return redirect('GALERIA')
    except:
        print('No elimino')
    return render(request, 'galeria.html', contexto)


def modificar_atencion(request, id):
    atencion = regAte.objects.get(idAtencion = id)
    mecanico = Mecanico.objects.all()
    especialidad = Especialidad.objects.all()
    contexto = {
        "ate":atencion,
        "especialidades": especialidad,
        "mecanicos":mecanico
    }
    return render(request,'modificar_atenciones.html', contexto)
from datetime import datetime
@login_required(login_url='/login/')
def modificarDefinitivo(request):
    if request.POST:
        id = request.POST.get("txtId")
        mecanico = request.POST.get("cboMecanico")
        especialidad = request.POST.get("cboEspecialidad")
        titulo = request.POST.get("txtTitulo")
        descripcion = request.POST.get("txtDescripcion")
        materiales = request.POST.get("txtMateriales")
        fecha = request.POST.get("datFecha")
        foto = request.FILES.get("fileFoto")
        obj_esp = Especialidad.objects.filter(nombre = especialidad)
        usu = request.user.username
        usuario = User.objects.get(username=usu)
        ate = regAte.objects.get(idAtencion = id)
        ate.mecanico = mecanico
        ate.especialidad = obj_esp
        ate.titulo = titulo
        ate.descripcion = descripcion
        ate.materiales = materiales
        ate.fecha = fecha
        if foto is not None:
            ate.foto = foto
        ate.usuario = usuario
        ate.save()
    return render(request, 'index.html')

def grabar_galeria(request):
    if request.POST:
        id= request.POST.get("txtId")
        foto= request.FILES.get("txtFoto")
        atencion = regAte.objects.get(idAtencion = id)
        gale = Galeria(
            foto = foto,
            atencion= atencion
        )
        gale.save()
        return redirect("/galeria/")