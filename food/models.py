from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField(default=0)
    item_image = models.CharField(max_length=500, default="https://hcue.restaurant/assets/img/item/placeholder.jpg?v=1")

    def __str__(self):
        return self.item_name