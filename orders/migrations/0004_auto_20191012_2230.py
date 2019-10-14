# Generated by Django 2.0.3 on 2019-10-12 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191012_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Serving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='orders.Category'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='fooditem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='orders.Topping'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serving', to='orders.Serving'),
        ),
    ]