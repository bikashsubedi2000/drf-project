# views.py

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate

from .models import Category, Blog
from .serializers import CategorySerializer, BlogSerializer, RegisterSerializer

User = get_user_model()

# ---------- CATEGORY VIEWS ----------
class AddCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AddListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UpdateDeleteCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ---------- BLOG VIEWS ----------
class AddBlog(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ListBlog(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class RetrieveBlog(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class UpdateBlog(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    

class DeleteBlog(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# ---------- USER REGISTRATION ----------
class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# ---------- USER LOGIN ----------
class LoginUser(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            refreshtoken = RefreshToken.for_user(user)
            return Response({
                "email": user.email,
                "role": user.is_user,
                "refreshtoken": str(refreshtoken),
                "accesstoken": str(refreshtoken.access_token)
            })
        return Response({"error": "Invalid credential"}, status=status.HTTP_400_BAD_REQUEST)
