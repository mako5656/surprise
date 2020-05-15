from django_filters import FilterSet
from django_filters import filters

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    shop_name = filters.CharFilter(label='店名', lookup_expr='contains')
    
    fields=(
        ('shop_name','shop_name'),
        ('budget','budget'),
        ('area','area'),
    ),

    field_labels={
        'shop_name':'店名',
        'budget':'予算',
        'area':'エリア',
    },
    label='並び順'

    class Meta:
        model = Item
        fields = ('shop_name','budget','area')
