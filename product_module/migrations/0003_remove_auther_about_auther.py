# Generated by Django 4.2.6 on 2023-10-24 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_auther_remove_product_auther_product_auther'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auther',
            name='about_auther',
        ),
    ]
