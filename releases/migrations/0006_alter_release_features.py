# Generated by Django 5.0.7 on 2024-12-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_artist_options_alter_artist_description_and_more'),
        ('releases', '0005_release_features_alter_release_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='features', to='artists.artist', verbose_name='همکاری ها'),
        ),
    ]
