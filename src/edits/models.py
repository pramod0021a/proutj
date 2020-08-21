from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Edit(models.Model):
    name = models.CharField(max_length=50)
    ananda_vani = models.TextField()

    slider1_img = models.ImageField(blank=True, null=True)
    slider1_title = models.CharField(max_length=250)
    slider2_img = models.ImageField(blank=True, null=True)
    slider2_title = models.CharField(max_length=250)
    slider3_img = models.ImageField(blank=True, null=True)
    slider3_title = models.CharField(max_length=250)
    slider4_img = models.ImageField(blank=True, null=True)
    slider4_title = models.CharField(max_length=250)
    slider5_img = models.ImageField(blank=True, null=True)
    slider5_title = models.CharField(max_length=250)
    slider6_img = models.ImageField(blank=True, null=True)
    slider6_title = models.CharField(max_length=250)

    recent1_title = models.CharField(max_length=250)
    recent1_img = models.ImageField(blank=True, null=True)
    recent1_pdf = models.FileField(blank=True, null=True)
    recent2_title = models.CharField(max_length=250)
    recent2_img = models.ImageField(blank=True, null=True)
    recent2_pdf = models.FileField(blank=True, null=True)
    recent3_title = models.CharField(max_length=250)
    recent3_img = models.ImageField(blank=True, null=True)
    recent3_pdf = models.FileField(blank=True, null=True)

    act1_img = models.ImageField(blank=True, null=True)
    act1_title = models.CharField(max_length=250)
    act1_desc = RichTextUploadingField()
    act2_img = models.ImageField(blank=True, null=True)
    act2_title = models.CharField(max_length=250)
    act2_desc = RichTextUploadingField()
    act3_img = models.ImageField(blank=True, null=True)
    act3_title = models.CharField(max_length=250)
    act3_desc = RichTextUploadingField()
    act4_img = models.ImageField(blank=True, null=True)
    act4_title = models.CharField(max_length=250)
    act4_desc = RichTextUploadingField()
    act5_img = models.ImageField(blank=True, null=True)
    act5_title = models.CharField(max_length=250)
    act5_desc = RichTextUploadingField()
    act6_img = models.ImageField(blank=True, null=True)
    act6_title = models.CharField(max_length=250)
    act6_desc = RichTextUploadingField()

    current_img = models.ImageField(blank=True, null=True)
    current_pdf = models.FileField(blank=True, null=True)

    editorial_title = models.CharField(max_length=50)
    editorial_intro = models.TextField(blank=True, null=True)
    editorial_desc = RichTextUploadingField()

    coverstory_title = models.CharField(max_length=50)
    coverstory_writer = models.CharField(default="", max_length=50)
    coverstory_intro = models.TextField(blank=True, null=True)
    coverstory_desc = RichTextUploadingField()
    coverstory_img = models.ImageField(default="", blank=True, null=True)

    ad_img = models.ImageField(blank=True, null=True)

    partner1_img = models.ImageField(blank=True, null=True)
    partner1_title = models.CharField(max_length=20)
    partner2_img = models.ImageField(blank=True, null=True)
    partner2_title = models.CharField(max_length=20)
    partner3_img = models.ImageField(blank=True, null=True)
    partner3_title = models.CharField(max_length=20)
    partner4_img = models.ImageField(default="", blank=True, null=True)
    partner4_title = models.CharField(default="", max_length=20)

    editor = models.CharField(max_length=50)
    editorial_board = models.CharField(max_length=100)
    general_manager = models.CharField(max_length=50)
    business_director = models.CharField(max_length=50)
    circular_manager = models.CharField(max_length=50)
    correspondents = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return self.name
