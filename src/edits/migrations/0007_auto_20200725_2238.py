# Generated by Django 3.0.7 on 2020-07-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edits', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
