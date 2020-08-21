# Generated by Django 3.0.7 on 2020-07-20 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_title', models.CharField(max_length=200)),
                ('pub_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('pub_buy', models.URLField()),
            ],
        ),
    ]
