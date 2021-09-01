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
    count = models.IntegerField(verbose_name="Колмчество продуктов")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_product')

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"count: {str(self.count)}, name: {self.name}"



class AccountingForPurchases(models.Model):
    pass


class AccountingForSupplies(models.Model):
    pass
