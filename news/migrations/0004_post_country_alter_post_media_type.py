# Generated by Django 4.0.1 on 2022-01-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_continent_post_media_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='media_type',
            field=models.CharField(choices=[('broadcast', 'Broadcast'), ('internet', 'Internet'), ('magazine', 'Magazine'), ('newspaper', 'Newspaper'), ('press-agency', 'Press Agency'), ('news', 'News')], default='news', max_length=500),
        ),
    ]
