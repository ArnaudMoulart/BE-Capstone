# Generated by Django 5.0.2 on 2024-03-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_menu_menu_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]