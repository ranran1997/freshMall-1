# Generated by Django 2.0.5 on 2018-05-10 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20180510_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_sn',
            field=models.CharField(default='', max_length=50, verbose_name='商品货号'),
        ),
    ]