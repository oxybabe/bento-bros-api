# Generated by Django 4.2.2 on 2023-06-22 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0007_alter_appetizer_price_alter_dessert_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appetizer',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='dessert',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='maincourse',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
    ]
