from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    def __str__(self):
        return self.category_name
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    price=models.DecimalField(decimal_places=2,max_digits=7)
    description=models.TextField()
    image=models.ImageField(upload_to='products/',blank=True,null=True)
    stock=models.PositiveIntegerField(default=0)
    avaible=models.BooleanField(default=True)
    def __str__(self):
        return self.name

