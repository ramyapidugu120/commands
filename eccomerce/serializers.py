from .models import (Category,
                    Products,
                    CustomerDetails,
                    Orders,
                    OrderItems,
                    Payment)
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','category_name')

class ProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Products
        fields='__all__'

class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerDetails
        fields='__all__'

class OrdersSerializer(serializers.ModelSerializer):
    customer_name=serializers.CharField(source='CustomerID.customer_name')
    
    class Meta:
        model=Orders
        fields='__all__'

class OrderItemsSerializer(serializers.ModelSerializer):
    ProductName=serializers.CharField(source='ProductID.ProductName',read_only=True)
    ProductPrice=serializers.CharField(source='ProductID.ProductPrice', read_only=True)

    class Meta:
        model=OrderItems
        fields = ['OrderItemsID', 'OrderID', 'ProductID', 'Quantity','ProductName','ProductPrice']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'

