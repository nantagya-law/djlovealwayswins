from django.db import models

# Create your models here.
class Donate(models.Model):
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=4, decimal_places=2) 
    
    def ___str__(self):
        return self.title
