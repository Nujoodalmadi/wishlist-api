from django.shortcuts import render

from items.models import Item
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from .serializers import (
    ItemListSerializer,
    ItemDetailSerializer,
)

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import (AllowAny, IsAuthenticated, )
from .permissions import IsAdder

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    filter_backends = [OrderingFilter, SearchFilter,]
    search_fields = ['image', 'name', 'description']
    permission_classes = [AllowAny,]


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes= [IsAuthenticated, IsAdder,]
