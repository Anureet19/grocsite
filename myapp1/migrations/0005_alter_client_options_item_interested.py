# Generated by Django 4.1.5 on 2023-03-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0004_alter_orderitem_order_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client'},
        ),
        migrations.AddField(
            model_name='item',
            name='interested',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
