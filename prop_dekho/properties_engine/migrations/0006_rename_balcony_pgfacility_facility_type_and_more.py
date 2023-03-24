# Generated by Django 4.1.7 on 2023-03-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties_engine', '0005_pgtype_latestpg_pg_facility_remove_latestpg_pgtype_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pgfacility',
            old_name='Balcony',
            new_name='facility_type',
        ),
        migrations.RemoveField(
            model_name='pgfacility',
            name='ac',
        ),
        migrations.RemoveField(
            model_name='pgfacility',
            name='cupboard',
        ),
        migrations.RemoveField(
            model_name='pgfacility',
            name='dth',
        ),
        migrations.RemoveField(
            model_name='pgfacility',
            name='mattress',
        ),
        migrations.RemoveField(
            model_name='pgfacility',
            name='side_table',
        ),
        migrations.RemoveField(
            model_name='pgfacility',
            name='tv',
        ),
        migrations.RemoveField(
            model_name='pgfacility',
            name='washroom',
        ),
        migrations.RemoveField(
            model_name='pgfacility',
            name='wifi',
        ),
        migrations.AddField(
            model_name='pgfacility',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
