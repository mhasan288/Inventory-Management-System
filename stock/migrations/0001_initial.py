# Generated by Django 3.1.3 on 2020-11-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockBinModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_name', models.CharField(max_length=255, verbose_name='Bin Name')),
                ('goods_code', models.CharField(max_length=255, verbose_name='Goods Code')),
                ('goods_desc', models.CharField(max_length=255, verbose_name='Goods Description')),
                ('goods_qty', models.IntegerField(default=0, verbose_name='Binstock Qty')),
                ('bin_size', models.CharField(max_length=255, verbose_name='Bin size')),
                ('bin_property', models.CharField(max_length=255, verbose_name='Bin Property')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'data id',
                'verbose_name_plural': 'data id',
                'db_table': 'stockbin',
                'ordering': ['update_time'],
            },
        ),
        migrations.CreateModel(
            name='StockListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_code', models.CharField(max_length=32, verbose_name='Goods Code')),
                ('goods_desc', models.CharField(max_length=255, verbose_name='Goods Description')),
                ('goods_qty', models.BigIntegerField(default=0, verbose_name='Total Qty')),
                ('onhand_stock', models.BigIntegerField(default=0, verbose_name='On Hand Stock')),
                ('can_order_stock', models.BigIntegerField(default=0, verbose_name='Can Order Stock')),
                ('inspect_stock', models.BigIntegerField(default=0, verbose_name='Inspect Stock')),
                ('cross_dock_stock', models.BigIntegerField(default=0, verbose_name='Cross Dock Stock')),
                ('hold_stock', models.BigIntegerField(default=0, verbose_name='Holding Stock')),
                ('damage_stock', models.BigIntegerField(default=0, verbose_name='Damage Stock')),
                ('asn_stock', models.BigIntegerField(default=0, verbose_name='ASN Stock')),
                ('pre_load_stock', models.BigIntegerField(default=0, verbose_name='Pre Load Stock')),
                ('pre_sort_stock', models.BigIntegerField(default=0, verbose_name='Pre Sort Stock')),
                ('sorted_stock', models.BigIntegerField(default=0, verbose_name='Sorted Stock')),
                ('pick_stock', models.BigIntegerField(default=0, verbose_name='Pick Stock')),
                ('picked_stock', models.BigIntegerField(default=0, verbose_name='Picked Stock')),
                ('back_order_stock', models.BigIntegerField(default=0, verbose_name='Back Order Stock')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'data id',
                'verbose_name_plural': 'data id',
                'db_table': 'stocklist',
                'ordering': ['update_time'],
            },
        ),
    ]
