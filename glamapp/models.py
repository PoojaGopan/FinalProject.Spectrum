from django.db import models

class Categories(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Brand(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
from django.db import models
class Filter_prize(models.Model):
    FILTER_PRIZE = [
        ('below ₹250', 'below ₹250'),
        ('below ₹500', 'below ₹500'),
        ('below ₹1000', 'below ₹1000'),
        ('below ₹2000', 'below ₹2000'),
    ]
    prize = models.CharField(choices=FILTER_PRIZE, max_length=200)
    def __str__(self):
        return self.prize
class Product(models.Model):
    CONDITION=(('new','new'),('old','old'))
    STOCK=(('stock-in','stock-in'),('stock-out','stock-out'))
    STATUS=(('publish','publish'),('draft','draft'))
    unique_id=models.CharField(unique=True,max_length=200,null=False)
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    condition=models.CharField(choices=CONDITION,max_length=100)
    information=models.TextField()
    deescription=models.TextField()
    stock=models.CharField(choices=STOCK,max_length=200)
    status=models.CharField(choices=STATUS,max_length=200)
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    filter_price=models.ForeignKey(Filter_prize,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Images (models.Model):
    image= models. ImageField(upload_to='pics')
    product =models.ForeignKey(Product ,on_delete=models.CASCADE)

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField(max_length=200)
    def __str__(self):
        return self.name
    
from django.contrib.auth.models import User
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    address=models.TextField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    postcode=models.ImageField(max_length=200)
    phone=models.IntegerField()
    amount=models.CharField(max_length=200)
    payment_id=models.CharField(max_length=200,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    email=models.EmailField(max_length=200)
    def __str__(self):
        return self.user.username
    
class Orderitem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics')
    quantity=models.CharField(max_length=200)
    prize =models.CharField(max_length=200)
    total=models.CharField(max_length=200)
    def __str__(self):
        return self.order.user.username