# Generated by Django 4.0.1 on 2022-01-06 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_post_image_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='continent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='media_type',
            field=models.CharField(blank=True, choices=[('broadcast', 'Broadcast'), ('internet', 'Internet'), ('magazine', 'Magazine'), ('newspaper', 'Newspaper'), ('press-agency', 'Press Agency'), ('news', 'News')], default='news', max_length=500, null=True),
        ),
    ]
