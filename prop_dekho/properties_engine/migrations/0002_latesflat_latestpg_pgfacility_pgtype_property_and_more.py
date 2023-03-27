
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties_engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatesFlat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_name', models.IntegerField(choices=[(1, '1BHK'), (2, '2BHK'), (3, '3BHK'), (4, '4BHK')])),
                ('flat_image', models.ImageField(upload_to='latest/flat_image/', verbose_name='Flat Image')),
                ('flat_rent', models.CharField(max_length=200)),
                ('area', models.IntegerField()),
                ('flat_location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LatestPg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg_image', models.ImageField(upload_to='latestpg/latestpg_image/', verbose_name='Pg Image')),
                ('pg_location', models.CharField(max_length=255)),
                ('pg_rent', models.FloatField()),
                ('pg_name', models.CharField(max_length=255)),
                ('ac', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('washroom', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('dth', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('wifi', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('matress', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('cupboard', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('side_table', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('balcony', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='PgFacility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('facility_type', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PgType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_image', models.ImageField(upload_to='property/feature_image/', verbose_name='Feature Image')),
                ('location', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('li_title1', ckeditor.fields.RichTextField()),
                ('no_of_bedroom', models.IntegerField(blank=True, null=True, verbose_name='Number of Bedroom')),
                ('li_title2', ckeditor.fields.RichTextField()),
                ('no_of_bathroom', models.IntegerField(blank=True, null=True, verbose_name='Number of Bathroom')),
                ('li_title3', ckeditor.fields.RichTextField()),
                ('no_of_kitchen', models.IntegerField(blank=True, null=True, verbose_name='Number of Kitchen')),
                ('author_image', models.ImageField(blank=True, null=True, upload_to='property/author_image/', verbose_name='Author Image')),
                ('author_name', models.CharField(blank=True, max_length=233, null=True, verbose_name='Author Name')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('description', models.TextField()),
                ('area', models.IntegerField()),
                ('cartegory', models.ManyToManyField(related_name='property_category', to='properties_engine.category')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties_engine.propertytype')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyForSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=200)),
                ('owner_name', models.CharField(max_length=200)),
                ('sale_image', models.ImageField(upload_to='propertysale/sale_image', verbose_name='Sale Image')),
                ('sale_price', models.FloatField()),
                ('sale_address', models.CharField(max_length=200)),
                ('sale_area', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Properity',
        ),
        migrations.AddField(
            model_name='latestpg',
            name='pgtype',
            field=models.ManyToManyField(related_name='pg_type', to='properties_engine.pgtype'),
        ),
    ]
