# Generated by Django 3.0.7 on 2020-07-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edits', '0003_auto_20200717_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='edit',
            name='coverstory_img',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]