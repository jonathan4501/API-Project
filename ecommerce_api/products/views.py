from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, User
from .serializers import ProductSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenVerifySerializer
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer

class CreateProductView(APIView):
    queryset = Product.objects.all()
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer]
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ReadProductView(APIView):
    queryset = Product.objects.all()

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)

        

class UpdateProductView(APIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class DeleteProductView(APIView):
    queryset = Product.objects.all()

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=204)

class CreateUserView(APIView):
    queryset = User.objects.all()
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ReadUserView(APIView):
    queryset = User.objects.all()

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UpdateUserView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class DeleteUserView(APIView):
    queryset = User.objects.all()

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=204)

class SearchProductView(APIView):
    def get(self, request):
        query = request.GET.get('q')
        products = Product.objects.filter(name__icontains=query)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ListProductView(APIView):
    queryset = Product.objects.all()

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class RetrieveProductView(APIView):
    queryset = User.objects.all()
    
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class VerifyTokenView(TokenVerifyView):
    serializer_class = TokenVerifySerializer

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        token = RefreshToken(refresh_token)
        access_token = token.access_token
        return Response({'access_token': str(access_token)})
