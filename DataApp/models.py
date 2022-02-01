from django.db import models

# Create your models here.


class CareerModle(models.Model):
    F_name = models.CharField(max_length=100)
    L_name = models.CharField(max_length=100)
    body = models.TextField( default='sfjdfjdfkjdsdk')



    def __str__(self):
        return f'{self.F_name} {self.L_name}'
