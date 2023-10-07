from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='INDEX'),
    path('mecanicos/', mecanicos, name='MECANICOS'),
    path('contacto/', contacto, name='CONTACTO'),
    path('producto/', producto, name='PRODUCTOS'),
    path('login/', login, name='LOGIN'),
    path('logout/', cerrar_sesion, name='LOGOUT'),
    path('registro/', registro, name='REGISTRO'),
    path('galeria/', galeria, name='GALERIA'),
    path('registrar_atencion/', registrar_atencion, name='REGISTRAR_ATENCION'),
    path('filtroNom/', filtro_nombre, name='FILTRO_NOM'),
    path('filtro_espe/',filtro_espe,name='FILTRO_ESPE'),
    path('perfil/',perfil,name='PERFIL'),
    path('ficha/<id_atencion>',ficha,name='FICHA'),

    #Carrito
    path('agregar_carrito/<id_producto>/',agregar_carrito, name = 'AC' ),
    path('restar_carrito/<id_producto>/',restar_carrito, name = 'RC' ),
    path('eliminar_carrito/<id_producto>/',eliminar_carrito, name = 'EC' ),
    path('vaciar',vaciar, name = 'VACIAR' ),

    # Más funciones
    path('eliminar/<id_atencion>/',eliminar,name='ELI'),
    path('modificar_atencion/<id>/',modificar_atencion,name='MODIFICAR_ATENCION'),
    path('modificar_definitivo/',modificarDefinitivo,name='MODEF'),
    path('grabar_galeria/',grabar_galeria,name='GG'),
]