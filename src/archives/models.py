from django.db import models

# Create your models here.


class Year(models.Model):
    year_name = models.CharField(max_length=50)

    def __str__(self):
        return self.year_name


class Magazine(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    mag_title = models.CharField(max_length=50)
    mag_img = models.ImageField(blank=True, null=True)
    mag_pdf = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.mag_title
