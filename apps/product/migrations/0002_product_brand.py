# Generated by Django 4.0.4 on 2022-05-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
