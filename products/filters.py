from django_filters import rest_framework as filters
from .models import Product

class ProductFilter(filters.FilterSet):
    name=filters.CharFilter(field_name="name",lookup_expr='icontains')
    category = filters.NumberFilter(field_name="category")
    class Meta:
        model=Product
        fields=('category','name')