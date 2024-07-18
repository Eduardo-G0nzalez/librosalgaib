# Generated by Django 4.2.14 on 2024-07-16 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_editorial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='descripcion',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='paginas',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
