from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя магазина")
    date_create = models.DateField(auto_now_add=True, verbose_name="Дата создание магазинв")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Продукт")
    date_create = models.DateField(auto_now_add=True, verbose_name="Дата создание магазинв")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"name: {self.name}"


class ProductsInTheStore(models.Model):
    store = models.ForeignKey(Store, related_name='store', on_delete=models.CASCADE)
    products = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="Колмчество продуктов")
    datetime = models.DateTimeField(auto_now_add=True)


class AccountingForPurchases(models.Model):
    pass


class AccountingForSupplies(models.Model):
    pass
