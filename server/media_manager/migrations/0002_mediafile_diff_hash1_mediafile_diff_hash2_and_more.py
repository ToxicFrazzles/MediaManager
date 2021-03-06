# Generated by Django 4.0.3 on 2022-04-18 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='diff_hash1',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='diff_hash2',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='diff_hash3',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='diff_hash4',
            field=models.BigIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='similar_to',
            field=models.ManyToManyField(default=None, related_name='similar_files', to='media_manager.mediafile'),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='x_resolution',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='y_resolution',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
