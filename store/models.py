from django.db import models

# Create your models here.
class Store(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.IntegerField()
  last_update = models.DateTimeField(auto_now=True)


class Collection(models.Model):
  title = models.CharField(max_length=255)

class Product(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  inventory = models.IntegerField()
  last_update = models.DateTimeField(auto_now=True)
  collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
  promotion = models.ManyToManyField('Promotion',  related_name='products')

class Order (models.Model):
  PAYMENT_STATUS_PENDING = 'P'
  PAYMENT_STATUS_COMPLETE = 'C'
  PAYMENT_STATUS_FAILED = 'F'
  PAYMENT_STATUS_CHOICES = [
    (PAYMENT_STATUS_PENDING, 'Pending'),
    (PAYMENT_STATUS_COMPLETE, 'Complete'),
    (PAYMENT_STATUS_FAILED, 'Failed')
  ]

  placed_at = models.DateTimeField(auto_now_add=True)
  payment_status = models.CharField(choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING, max_length=1)
  customer = models.ForeignKey("Customer", on_delete=models.PROTECT)

class Promotion(models.Model):
  description = models.CharField(max_length=255)
  discount = models.FloatField()


class Customer(models.Model):
  MEMBERSHIP_Bronze = 'B'
  MEMBERSHIP_Silver = 'S'
  MEMBERSHIP_Gold = 'G'
  MEMBERSHIP_CHOICES = [
    (MEMBERSHIP_Bronze, 'Bronze'),
    (MEMBERSHIP_Silver, 'Silver'),
    (MEMBERSHIP_Gold, 'Gold'),
  ]
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=255)
  birth_date = models.DateField()
  membership = models.CharField(choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_Bronze, max_length=1)



class Address(models.Model):
  street = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)



class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.PROTECT)
  product = models.ForeignKey(Product, on_delete=models.PROTECT)
  quantity = models.PositiveSmallIntegerField()
  unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveSmallIntegerField()
