# Generated by Django 4.0.4 on 2022-05-09 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(verbose_name='date ordered')),
                ('estimated_time', models.IntegerField(default=-1)),
                ('delivery_address', models.CharField(max_length=100)),
                ('delivery_finish', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=50)),
                ('shop_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order_menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_menu_name', models.CharField(max_length=30)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.shop'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=30)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.shop')),
            ],
        ),
    ]
