from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='категория')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    
    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=20, verbose_name="название")
    description = models.TextField(max_length=200, verbose_name = 'описание', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=False)
    price = models.DecimalField(max_digits=1000, decimal_places=2)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.name}'


class Cart(models.Model):
    owner = models.CharField(max_length=50)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

    def __str__(self):
        return f'{self.owner} - {self.total_price}'