# Generated by Django 3.2.7 on 2021-11-02 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='id_restau',
            new_name='name',
        ),
    ]
