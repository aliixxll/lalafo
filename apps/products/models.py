from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название продукта"
    )
    description = models.TextField(
        verbose_name = "Описание продукта"
    )
    image = models.ImageField(
        upload_to = 'product_image/',
        verbose_name = "Фотография продукта"
    )
    price = models.PositiveIntegerField(
        verbose_name = "Цена продукта"
    )
    created = models.DateTimeField(
        auto_now_add = True
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"