# Generated by Django 5.0.7 on 2024-12-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_profile_options_and_more'),
        ('releases', '0005_release_features_alter_release_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='listening_history',
            field=models.ManyToManyField(blank=True, related_name='listening_history', to='releases.release', verbose_name='تاریخچه پخش'),
        ),
    ]
