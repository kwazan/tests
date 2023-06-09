# Generated by Django 4.1.5 on 2023-01-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0021_rename_name_payment_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('user_ip', models.GenericIPAddressField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='payment',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user_ip',
        ),
    ]