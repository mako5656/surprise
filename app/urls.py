from django.urls import path
from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView
from . import cover

urlpatterns = [
    path('surprise/',  ItemFilterView.as_view(), name='index'),
    path('create/', ItemCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),

    path('', cover.post_list, name='post_list'),
    path('cover2/', cover.post_list2, name='post_list2'),
]