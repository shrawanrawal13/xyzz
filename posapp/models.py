from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.


#supplier list
class Supplier(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=250, null= True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    mobile_no = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


#customer list
class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)   
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=20, blank=True, null=True)
    customer_type=models.CharField(max_length=200, default='customer', blank=True, null=True)
    address = models.TextField(max_length=500, blank=True,null=True)

    def save(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='customer')
        self.user.groups.add(group)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.customer_name





category_type = (
    ("Convenience", "Convenience"),
    ("shopping", "shopping"),

)

#product category
class Category(models.Model):
    title = models.CharField(max_length=100)
    category_type = models.CharField(max_length=100, choices=category_type)


    def __str__(self):
        return self.title


class Product(models.Model):
    UNIT_TYPE_KG = 'Kilogram'
    UNIT_TYPE_GRAM = 'Gram'
    UNIT_TYPE_LITRE = 'Litre'
    UNIT_TYPE_QUANTITY = 'Quantity'

    UNIT_TYPES = (
        (UNIT_TYPE_KG, 'Kilogram'),
        (UNIT_TYPE_GRAM, 'Gram'),
        (UNIT_TYPE_LITRE, 'Litre'),
        (UNIT_TYPE_QUANTITY, 'Quantity'),
    )
    unit_type = models.CharField(
        choices=UNIT_TYPES, default=UNIT_TYPE_QUANTITY,
        blank=True, null=True, max_length=200
    )
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name