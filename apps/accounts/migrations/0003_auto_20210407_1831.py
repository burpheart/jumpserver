# Generated by Django 3.1 on 2021-04-07 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210329_1649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'permissions': [('view_account_secret', 'Can view the secret of account')]},
        ),
    ]