# Generated by Django 5.0.7 on 2024-09-17 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_artist_options_alter_artist_description_and_more'),
        ('events', '0005_event_in_progress'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'رویداد', 'verbose_name_plural': 'رویداد ها'},
        ),
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(verbose_name='محتوا'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=255, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(verbose_name='تاریخ رویداد'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to='events', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='event',
            name='in_progress',
            field=models.BooleanField(default=True, verbose_name='در حال جریان'),
        ),
        migrations.AlterField(
            model_name='event',
            name='related_artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artists.artist', verbose_name='هنرمند مرتبط'),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(verbose_name='پیوندک'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255, verbose_name='عنوان'),
        ),
    ]
