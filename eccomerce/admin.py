from django.contrib import admin
from .models import (Category,
                    Products,
                    CustomerDetails,
                    Orders,
                    OrderItems,
                    Payment)

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(CustomerDetails)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(Payment)
