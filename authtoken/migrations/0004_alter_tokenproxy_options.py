# Generated by Django 4.1.3 on 2022-11-24 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tokenproxy',
            options={'verbose_name': 'Token', 'verbose_name_plural': 'Tokens'},
        ),
    ]
