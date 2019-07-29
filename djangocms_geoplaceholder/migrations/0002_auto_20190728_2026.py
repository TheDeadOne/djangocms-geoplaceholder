# Generated by Django 2.1 on 2019-07-28 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_geoplaceholder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoplaceholdermodel',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_geoip.City', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='geoplaceholdermodel',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_geoplaceholder_geoplaceholdermodel', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='geoplaceholdermodel',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_geoip.Country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='geoplaceholdermodel',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_geoip.Region', verbose_name='Регион'),
        ),
    ]
