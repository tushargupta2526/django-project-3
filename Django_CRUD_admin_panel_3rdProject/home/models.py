from django.db import models
from numpy import product

# Create your models here.
class Product(models.Model):
    product_id=models.IntegerField()
    name=models.TextField()
    description=models.TextField()
    price=models.FloatField()
    product_picture=models.ImageField()

    def __str__(self) -> str:
        return str(self.product_id)+' '+self.name+' '+str(self.price)

    class Meta:
        db_table='products'    