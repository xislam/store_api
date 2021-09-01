from rest_framework import serializers

from api_store_v1.models import Store, Product


class StoreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    date_create = serializers.DateField()
    store_product = serializers.StringRelatedField(many=True)

    class Meta:
        model = Store
        fields = ('id', 'name', 'date_create', 'store_product')


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
    count = serializers.IntegerField()

    class Meta:
        model = Store
        fields = ('name', 'store', 'count')



