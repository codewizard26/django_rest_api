from . models import Category
from . serializers import CategorySerializer
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset= Category.objects.all().order_by('name')
