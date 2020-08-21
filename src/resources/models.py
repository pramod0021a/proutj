from django.db import models

# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=30)
    item_icon = models.ImageField(default="",  blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    item_title = models.CharField(max_length=200)
    item_img = models.ImageField(blank=True, null=True)
    item_link = models.URLField(max_length=250, null=True)

    def __str__(self):
        return self.item_title
