from rest_framework import serializers

from api_store_v1.models import Store, Product


class StoreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    date_create = serializers.DateField(auto_now_add=True)

    class Meta:
        model = Store
        fields = ['name', 'date_create']


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
    count = serializers.IntegerField()

    class Meta:
        model = Store
        fields = '__all__'
