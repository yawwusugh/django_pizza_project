# Generated by Django 2.0.3 on 2019-10-19 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_merge_20191019_0900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='menuitem',
        ),
    ]