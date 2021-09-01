from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api_store_v1.models import Store, Product
from api_store_v1.serializers import StoreSerializer


class StoreViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing  Store.
    """

    def list(self, request):
        queryset = Store.objects.all()
        serializer = StoreSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, store_id=None):
        queryset = Store.objects.all().prefetch_related('store_product')
        store = get_object_or_404(queryset, pk=store_id)
        serializer = StoreSerializer(store)
        return Response(serializer.data)


