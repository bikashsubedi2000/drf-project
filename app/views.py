
# Create your views here.
# from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
# for add category 
class AddCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# for checking category list 
class CategoryList(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
# for add list category
class AddListCategory(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
#for updatedelete
class UpdateDeleteCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
    
    
    
    
    
    
class AddBlog(generics.CreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer         
    
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
       