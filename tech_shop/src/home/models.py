from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price =models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name
