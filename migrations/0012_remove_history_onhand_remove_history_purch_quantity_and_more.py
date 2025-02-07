# Generated by Django 5.1.1 on 2024-12-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_manage', '0011_remove_history_timestamp_alter_history_last_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='onhand',
        ),
        migrations.RemoveField(
            model_name='history',
            name='purch_quantity',
        ),
        migrations.RemoveField(
            model_name='history',
            name='sales_quantity',
        ),
        migrations.AddField(
            model_name='stock',
            name='history_category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='history_fs_number',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='history_issue_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='history_receive_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='history_targa_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='history_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='beg_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
