# Generated by Django 3.0.7 on 2020-07-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edits', '0004_edit_coverstory_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='edit',
            name='coverstory_writer',
            field=models.CharField(default='', max_length=50),
        ),
    ]
