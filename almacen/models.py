from django.db import models

# Create your models here.

#class Clientes(models.Model):
#    nombre=models.CharField(max_length=30)
#    direccion=models.CharField(max_length=50)
#    email=models.EmailField()
#    telefono=models.CharField(max_length=7)

class SeccionProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="seccionProd"
        verbose_name_plural="seccionesProd"

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.ForeignKey(SeccionProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="almacen", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    cantidad=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name="Articulo"
        verbose_name_plural="Articulos"



#class Pedidos(models.Model):
#    numero=models.IntegerField()
#    fecha=models.DateField()
#    entregado=models.BooleanField()


