# Generated by Django 3.2.7 on 2021-10-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicativoCRUD', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='Ano',
            field=models.IntegerField(),
        ),
    ]
