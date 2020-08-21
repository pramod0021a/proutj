from django.db import models

# Create your models here.


class Publication(models.Model):
    pub_title = models.CharField(max_length=200)
    pub_img = models.ImageField(blank=True, null=True)
    pub_buy = models.URLField(max_length=200)

    def __str__(self):
        return self.pub_title
