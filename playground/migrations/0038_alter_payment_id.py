# Generated by Django 4.1.6 on 2023-02-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0037_alter_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
