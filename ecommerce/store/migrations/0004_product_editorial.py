# Generated by Django 4.2.14 on 2024-07-16 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='editorial',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
