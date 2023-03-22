# Generated by Django 4.1.7 on 2023-03-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties_engine', '0008_latesflat_alter_latestpg_ac_alter_latestpg_balcony_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='latesflat',
            name='area',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='latesflat',
            name='flat_image',
            field=models.ImageField(default=1, upload_to='latest/flat_image/', verbose_name='Flat Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='latesflat',
            name='flat_name',
            field=models.IntegerField(choices=[(1, '1BHK'), (2, '2BHK'), (3, '3BHK'), (4, '4BHK')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='latesflat',
            name='flat_rent',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='latesflat',
            name='location',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
