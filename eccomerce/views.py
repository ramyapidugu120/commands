from .models import (Category,
                    Products,
                    CustomerDetails,
                    Orders,
                    OrderItems,
                    Payment)
from .serializers import (CategorySerializer,
                         ProductsSerializer,
                         CustomerDetailsSerializer,
                         OrdersSerializer,
                         OrderItemsSerializer,
                         PaymentSerializer)
from rest_framework import serializers
from rest_framework import  generics
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .permissions import IsOwner  # Import your custom permission
from rest_framework.pagination import PageNumberPagination 
 

# class Login(APIView):
#     permission_classes = [AllowAny]  # Allow unauthenticated access

#     def post(self, request, format=None):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'message': 'Login successful'
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class AllOrdersViewSet(APIView):
    def get(self, request, *args, **Kwargs):
        orders=Orders.objects.all()
        orders_data=OrdersSerializer(orders,many=True).data
         
        for order in orders_data:
            order['products']=OrderItemsSerializer(OrderItems.objects.filter(OrderID=order['OrderID']),many=True).data
        return Response(orders_data)

class RegCustomers(APIView):
    def post(self,request, *args, **Kwargs):
        reg_serializer=CustomerDetailsSerializer(data=request.data)

        if reg_serializer.is_valid():
            try:
                reg_serializer.save()
                return Response('user registered successfully',status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                if "UNIQUE constraint failed" in str(e):
                    return Response({"error": "Student with these credentials already exists."}, status=status.HTTP_409_CONFLICT)
                else:
                    return Response({"error": "Database error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddProducts(APIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    
    def post(self,request, *args, **Kwargs):
        addproducts_serializer=ProductsSerializer(data=request.data)

        if addproducts_serializer.is_valid():
            try:
                addproducts_serializer.save()
                return Response('product added successfully',status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response('product alrady exsist',status=status.HTTP_409_CONFLICT)
        else:
            return Response(addproducts_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class GetRequestedData(APIView):               # query params and pagination 
    def get(self, request, *args, **Kwargs):
        param=request.query_params.get('category')
        products=Products.objects.filter(category__category_name__iexact=param).order_by('ProductID') 
        pagination=PageNumberPagination()
        result_page=pagination.paginate_queryset(products,request)   #brings out the page number in queryparams
        data=ProductsSerializer(result_page,many=True).data

        return pagination.get_paginated_response(data)


class OwnerTask(APIView):
    queryset=Products.objects.all()
    serializer_class=ProductsSerializer

    permission_classes=[IsAuthenticated,IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) #set owner


class ProductView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ProductsSerializer


    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(owner=request.user)  # Set the owner here
                return Response({
                    'message':"data adaded successfully",
                    'data':serializer.data
                }, status=201)
            except IntegrityError as e:
                return Response('data already exists',status=status.HTTP_409_CONFLICT)

        return Response(serializer.errors, status=400)


    def get(self, request, pk=None):
        if pk:
            try:
                product = Products.objects.get(pk=pk)
                self.check_object_permissions(request, product) #check object level permissions
                serializer = ProductsSerializer(product)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response({"error": "Product not found."}, status=404)
        else:
            products = Products.objects.all()
            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data)

    
class Productdetail(APIView):
    permission_classes=[IsAuthenticated,IsOwner]

    def put(self, request, pk=None):
        product = Products.objects.get(pk=pk)
        try:
            self.check_object_permissions(request, product) #check object level permissions
            serializer = ProductsSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({ 
                    'message':'data added sucessfully',
                    'data':serializer.data},
                status=status.HTTP_201_CREATED)
            return Response({
                "message":'invalid data',
                "data":serializer.errors}, 
                status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=404)

    def patch(self, request, pk=None):
        product = Products.objects.get(pk=pk)
        try:
            self.check_object_permissions(request, product) #check object level permissions
            serializer = ProductsSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=404)


    def delete(self, request, pk=None):
        product = Products.objects.get(ProductID=pk)
        try:
            self.check_object_permissions(request, product)  # if object-level permissions
            product.delete()
            return Response({'message': 'deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Products.DoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)


   





