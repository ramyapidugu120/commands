from django.db import models
import uuid

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255)
    ProductDescription = models.TextField()
    ProductPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ProductWeight = models.DecimalField(max_digits=10, decimal_places=2)
    ProductUnits = models.CharField(max_length=255)
    ProductSize = models.CharField(max_length=255)
    ProductColor = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    owner=models.CharField(max_length=255,default='admin1')

    class Meta:
        unique_together=("ProductName","category")

    def __str__(self):
        return self.ProductName

class CustomerDetails(models.Model):
    customer_id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    customer_name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    address=models.TextField(blank=True,null=True)
    phone_number=models.CharField(max_length=200, blank=True, null=True,unique=True)
    email=models.EmailField(blank=True, null=True,unique=True)

    def __str__(self):
        return self.customer_name

class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    OrderDate = models.DateField()
    ShipDate = models.DateField()
    OrderTotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.OrderID)

class OrderItems(models.Model):
    OrderItemsID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField()

    def __str__(self):
        return str(self.OrderItemsID)

class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    PaymentDate = models.DateField()
    PaymentAmount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentMethod = models.CharField(max_length=255)

    def __str__(self):
        return str(self.PaymentID)
        
    
