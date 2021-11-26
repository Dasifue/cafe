# Generated by Django 3.2.8 on 2021-11-07 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in progress', 'In progress'), ('done', 'Done')], default='in progress', max_length=15)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
            },
        ),
    ]
