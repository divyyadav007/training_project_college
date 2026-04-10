from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length = 50)
    email =models.CharField(max_length = 100)
    phone = models.CharField(max_length = 15)
    message = models.CharField(max_length = 500)

    def __str__(self):
        return self.name

# class Product(models.Model):
#     name = models.CharField(max_length = 100)
#     description = models.TextField()
#     price = models.DecimalField(max_digit =  10 , decimal_places =2)
#     category = models.CharField(max_length = 50, choices =[('Milk', 'Milk'), ('Ghee', 'Ghee'), ('Curd', 'Curd')])
#     image = models.Imagefield(upload_to='products/')
#     stock_quantity = models.IntegerField(default = 0)

#     def __str__(self):
#         return self.name