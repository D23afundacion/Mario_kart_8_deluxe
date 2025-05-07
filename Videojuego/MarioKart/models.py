from django.db import models

class Usuarios(models.Model):
    id = models.IntegerField()
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    monedas = models.IntegerField()

class Copas (models.Model):
    id = models.IntegerField()
    nombre = models.CharField(max_length=100)
    img = models.TextField()

class Pistas (models.Model):
    id = models.IntegerField()
    nombre = models.CharField(max_length=100)
    img = models.TextField()
    copa_id = models.ForeignKey(Copas.id , on_delete=models.DO_NOTHING)

class Equipamientos(models.Model):
    id = models.IntegerField()
    nombre = models.CharField(max_length=100)
    img = models.TextField()
    tipo_equipamiento = [
        ('corredor_ligero', 'Corredor ligero'),
        ('corredor_medio', 'Corredor medio'),
        ('corredor_pesado', 'Corredor pesado'),
        ('vehículo', 'Vehículo'),
        ('ruedas', 'Ruedas'),
        ('ala_delta', 'Ala delta')
    ]
    tipo = models.CharField(max_length=20, choices=tipo_equipamiento)
    velocidad = models.IntegerField()
    aceleracion = models.IntegerField()
    peso  = models.IntegerField()
    manejo = models.IntegerField()
    agarre = models.IntegerField()
    precio = models.IntegerField()

class Records(models.Model):
    posicion = models.IntegerField()
    tiempo = models.CharField(max_length=100)
    usuario_id = models.ForeignKey(Usuarios.id, on_delete=models.DO_NOTHING)
    pista_id = models.ForeignKey(Pistas.id, on_delete=models.DO_NOTHING)

class Adquiridos(models.Model):
    usuario_id = models.ForeignKey(Usuarios.id, on_delete=models.DO_NOTHING)
    equipamiento_id = models.ForeignKey(Equipamientos.id, on_delete=models.DO_NOTHING)