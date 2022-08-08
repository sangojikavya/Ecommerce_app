# Generated by Django 4.0.5 on 2022-07-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, unique=True)),
                ('Slug', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(max_length=255)),
                ('images', models.ImageField(upload_to='images/category')),
            ],
        ),
    ]
