from django.db import models

# Create your models here.


class Download(models.Model):
    name = models.CharField(max_length=50)
    item_icon = models.ImageField(default="",  blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    download = models.ForeignKey(Download, on_delete=models.CASCADE)
    item_title = models.CharField(max_length=100)
    item_link = models.URLField(max_length=250)

    def __str__(self):
        return self.item_title
