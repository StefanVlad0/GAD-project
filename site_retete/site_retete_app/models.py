from django.db import models

# Create your models here.

class Reteta(models.Model):
    nume = models.CharField(max_length=200)
    timp = models.CharField(max_length=50)
    dificultate = models.CharField(max_length=20)
    ingrediente = models.TextField()

    def __str__(self):
        return self.nume