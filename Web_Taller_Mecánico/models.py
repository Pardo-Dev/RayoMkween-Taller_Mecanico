from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Especialidad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, null=True)
    descripcion = models.TextField(default="---")
    foto = models.ImageField(upload_to='especialidad', null=True)
    def __str__(self):
        return self.nombre

class Mecanico(models.Model):
    rut = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    edad = models.IntegerField()
    descripcion = models.TextField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    foto=models.ImageField(upload_to='mecanico',null=True)
    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=45)
    correo = models.EmailField()
    fono = models.IntegerField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    
class regAte(models.Model):
    idAtencion = models.AutoField(primary_key=True)
    tipoAte = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    rutMeca = models.ForeignKey(Mecanico, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=45)
    descAte = models.TextField()
    materiales = models.TextField()
    fecha = models.DateField()
    foto = models.ImageField(upload_to="atenciones", null=True)
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
    
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField(default=1000)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="producto", null=True)

    def __str__(self):
        return self.nombre
    
class Galeria(models.Model):
    idGaleria= models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='foto')
    atencion = models.ForeignKey(regAte,on_delete=models.CASCADE)

    def __str_(self):
        return "N°" + str(self.idGaleria)+"/"+self.atencion.titulo