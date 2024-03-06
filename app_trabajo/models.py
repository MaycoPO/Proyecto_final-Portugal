from django.db import models

# Create your models here.

class electrodomesticos(models.Model):
    electrodomestico = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    compra = models.IntegerField()
    cliente = models.CharField(max_length=30)
    DNI = models.IntegerField()

    def __str__(self):
        return f"Compra: {self.compra} | DNI: {self.DNI} | Cliente: {self.cliente}"


