from django.db import models



class Book(models.Model):
    title      = models.CharField(max_length = 255)
    subtitle   =  models.CharField(max_length=100)
    author     =  models.CharField(max_length=100)
    isbn       =  models.CharField(max_length=100)
    price      =  models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return self.title