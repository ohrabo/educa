# Generated by Django 2.0.7 on 2018-07-25 20:18

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20180725_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='marker',
            name='address',
        ),
        migrations.RemoveField(
            model_name='marker',
            name='geolocation',
        ),
        migrations.AddField(
            model_name='marker',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='marker',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='marker',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='link',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marker',
            name='lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
