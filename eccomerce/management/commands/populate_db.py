from django.core.management.base import BaseCommand
import uuid
from datetime import date, datetime
from eccomerce.models import (
    Category,
    Products,  # Changed from Product to Products
    CustomerDetails,
    Orders,  # Changed from Order to Orders
    OrderItems,
    Payment,
)  # change to your app name


class Command(BaseCommand):
    help = "Populates the database with sample data"

    def handle(self, *args, **options):
        """
        Generates sample data for the e-commerce models.
        """

        # 1. Categories
        categories = [
            Category.objects.create(category_name="Electronics"),
            Category.objects.create(category_name="Clothing"),
            Category.objects.create(category_name="Home Goods"),
            Category.objects.create(category_name="Books"),
            Category.objects.create(category_name="Sports"),
        ]

        # 2. Products
        products = [  # Changed to use Products model
            Products.objects.create(
                ProductName="Laptop",
                ProductDescription="High-performance laptop",
                ProductPrice=1200.00,
                ProductWeight=2.5,
                ProductUnits="kg",
                ProductSize="15 inch",
                ProductColor="Space Gray",
                category=categories[0],
            ),
            Products.objects.create(
                ProductName="T-Shirt",
                ProductDescription="Cotton T-shirt",
                ProductPrice=25.00,
                ProductWeight=0.2,
                ProductUnits="piece",
                ProductSize="M",
                ProductColor="Blue",
                category=categories[1],
            ),
            Products.objects.create(
                ProductName="Sofa",
                ProductDescription="Comfortable sofa",
                ProductPrice=500.00,
                ProductWeight=50.0,
                ProductUnits="kg",
                ProductSize="Large",
                ProductColor="Beige",
                category=categories[2],
            ),
            Products.objects.create(
                ProductName="Python Book",
                ProductDescription="Learn Python programming",
                ProductPrice=30.00,
                ProductWeight=0.8,
                ProductUnits="piece",
                ProductSize="Standard",
                ProductColor="White",
                category=categories[3],
            ),
            Products.objects.create(
                ProductName="Basketball",
                ProductDescription="Official size basketball",
                ProductPrice=20.00,
                ProductWeight=0.6,
                ProductUnits="piece",
                ProductSize="Size 7",
                ProductColor="Orange",
                category=categories[4],
            ),
            Products.objects.create(
                ProductName="Smartphone",
                ProductDescription="Latest smartphone model",
                ProductPrice=1000.00,
                ProductWeight=0.15,
                ProductUnits="piece",
                ProductSize="6.1 inch",
                ProductColor="Black",
                category=categories[0],
            ),
            Products.objects.create(
                ProductName="Jeans",
                ProductDescription="Slim fit jeans",
                ProductPrice=60.00,
                ProductWeight=0.5,
                ProductUnits="piece",
                ProductSize="32",
                ProductColor="Denim Blue",
                category=categories[1],
            ),
            Products.objects.create(
                ProductName="Dining Table",
                ProductDescription="Wooden dining table",
                ProductPrice=300.00,
                ProductWeight=30.0,
                ProductUnits="kg",
                ProductSize="6ft",
                ProductColor="Brown",
                category=categories[2],
            ),
            Products.objects.create(
                ProductName="JavaScript Book",
                ProductDescription="Learn JavaScript programming",
                ProductPrice=25.00,
                ProductWeight=0.7,
                ProductUnits="piece",
                ProductSize="Standard",
                ProductColor="White",
                category=categories[3],
            ),
            Products.objects.create(
                ProductName="Soccer Ball",
                ProductDescription="Official size soccer ball",
                ProductPrice=22.00,
                ProductWeight=0.45,
                ProductUnits="piece",
                ProductSize="Size 5",
                ProductColor="White/Black",
                category=categories[4],
            ),
        ]

        # 3. Customers
        customers = [
            CustomerDetails.objects.create(
                customer_name="Alice Smith",
                address="123 Main St, Anytown, USA",
                phone_number="555-1234",
                email="alice.smith@example.com",
            ),
            CustomerDetails.objects.create(
                customer_name="Bob Johnson",
                address="456 Oak Ave, Someville, USA",
                phone_number="555-5678",
                email="bob.johnson@example.com",
            ),
            CustomerDetails.objects.create(
                customer_name="Charlie Brown",
                address="789 Pine Ln, Hilltop, USA",
                phone_number="555-9012",
                email="charlie.brown@example.com",
            ),
            CustomerDetails.objects.create(
                customer_name="Diana Miller",
                address="101 Elm St, ValleyView, USA",
                phone_number="555-3456",
                email="diana.miller@example.com",
            ),
            CustomerDetails.objects.create(
                customer_name="Ethan Davis",
                address="222 Cedar Rd, Riverdale, USA",
                phone_number="555-7890",
                email="ethan.davis@example.com",
            ),
            CustomerDetails.objects.create(
                customer_name="Fiona Green",
                address="333 Birch Ct, Lakeside, USA",
                phone_number="555-2345",
                email="fiona.green@example.com",
            ),
            CustomerDetails.objects.create(
                customer_name="George White",
                address="444 Maple Dr, Oceanview, USA",
                phone_number="555-6789",
                email="george.white@example.com",
            ),
            CustomerDetails.objects.create(
                customer_name="Hannah Black",
                address="555 Willow Way, MountainTop, USA",
                phone_number="555-0123",
                email="hannah.black@example.com",
            ),
            CustomerDetails.objects.create(
                customer_name="Isaac Gray",
                address="666 Oakwood Blvd, SunsetCity, USA",
                phone_number="555-4567",
                email="isaac.gray@example.com",
            ),
            CustomerDetails.objects.create(
                customer_name="Jessica Brown",
                address="777 Pinecrest Ave, SunriseTown, USA",
                phone_number="555-8901",
                email="jessica.brown@example.com",
            ),
        ]

        # 4. Orders and Order Items
        orders_data = [ # Changed to use Orders model
            {
                "customer": customers[0],
                "OrderDate": date(2024, 1, 20),
                "ShipDate": date(2024, 1, 25),
                "OrderTotal": 1400.00,
                "order_items": [
                    {"product": products[0], "Quantity": 1},  # Laptop
                    {"product": products[1], "Quantity": 2},  # T-Shirt
                ],
            },
            {
                "customer": customers[1],
                "OrderDate": date(2024, 2, 10),
                "ShipDate": date(2024, 2, 15),
                "OrderTotal": 525.00,
                "order_items": [
                    {"product": products[2], "Quantity": 1},  # Sofa
                    {"product": products[3], "Quantity": 5},  # Python Book
                ],
            },
            {
                "customer": customers[2],
                "OrderDate": date(2024, 3, 1),
                "ShipDate": date(2024, 3, 5),
                "OrderTotal": 200.00,
                "order_items": [{"product": products[4], "Quantity": 10}],  # Basketball
            },
            {
                "customer": customers[3],
                "OrderDate": date(2024, 1, 22),
                "ShipDate": date(2024, 1, 27),
                "OrderTotal": 2200.00,
                "order_items": [
                    {"product": products[5], "Quantity": 2},  # Smartphone
                    {"product": products[6], "Quantity": 2},  # Jeans
                ],
            },
            {
                "customer": customers[4],
                "OrderDate": date(2024, 2, 12),
                "ShipDate": date(2024, 2, 17),
                "OrderTotal": 900.00,
                "order_items": [
                    {"product": products[7], "Quantity": 3},  # Dining Table
                    {"product": products[8], "Quantity": 5},  # JavaScript Book
                ],
            },
             {
                "customer": customers[5],
                "OrderDate": date(2024, 3, 15),
                "ShipDate": date(2024, 3, 20),
                "OrderTotal": 220.00,
                "order_items": [
                    {"product": products[9], "Quantity": 10},  # Soccer Ball
                ],
            },
            {
                "customer": customers[6],
                "OrderDate": date(2024, 1, 25),
                "ShipDate": date(2024, 1, 30),
                "OrderTotal": 1250.00,
                "order_items": [
                    {"product": products[0], "Quantity": 1},  # Laptop
                    {"product": products[3], "Quantity": 1},  # Python Book
                ],
            },
            {
                "customer": customers[7],
                "OrderDate": date(2024, 2, 18),
                "ShipDate": date(2024, 2, 23),
                "OrderTotal": 110.00,
                "order_items": [
                    {"product": products[1], "Quantity": 4},  # T-Shirt
                ],
            },
            {
                "customer": customers[8],
                "OrderDate": date(2024, 3, 22),
                "ShipDate": date(2024, 3, 27),
                "OrderTotal": 650.00,
                "order_items": [
                    {"product": products[2], "Quantity": 1},  # Sofa
                    {"product": products[4], "Quantity": 5},  # Basketball
                ],
            },
            {
                "customer": customers[9],
                "OrderDate": date(2024, 1, 28),
                "ShipDate": date(2024, 2, 2),
                "OrderTotal": 2000.00,
                "order_items": [
                    {"product": products[5], "Quantity": 2},  # Smartphone
                ],
            },
        ]

        for order_data in orders_data:
            order = Orders.objects.create(  # Changed to Orders
                CustomerID=order_data["customer"],
                OrderDate=order_data["OrderDate"],
                ShipDate=order_data["ShipDate"],
                OrderTotal=order_data["OrderTotal"],
            )
            for item_data in order_data["order_items"]:
                OrderItems.objects.create(
                    OrderID=order,
                    ProductID=item_data["product"],
                    Quantity=item_data["Quantity"],
                )

        # 5. Payments (assuming one payment per order for simplicity)
        for order in Orders.objects.all():
            Payment.objects.create(
                OrderID=order,
                PaymentDate=order.OrderDate,  # Simplified: Payment on order date
                PaymentAmount=order.OrderTotal,
                PaymentMethod="Credit Card",  # Default payment method
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated database with sample data."))
