# Generated by Django 3.0.7 on 2020-07-26 08:40

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edits', '0008_auto_20200726_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit',
            name='act1_desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='edit',
            name='act2_desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='edit',
            name='act3_desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='edit',
            name='act4_desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='edit',
            name='act5_desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='edit',
            name='act6_desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='edit',
            name='coverstory_desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
