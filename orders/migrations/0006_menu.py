# Generated by Django 2.0.3 on 2019-10-12 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20191012_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='orders.Category')),
                ('fooditem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='orders.Topping')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serving', to='orders.Serving')),
            ],
        ),
    ]
