# Generated by Django 4.0.5 on 2022-07-20 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_rename_category_categorys'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categorys',
            new_name='category',
        ),
    ]
