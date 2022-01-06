import blank as blank
import null as null
from django.db import models
from django.forms.widgets import MEDIA_TYPES
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    STORY_TYPE_CHOICES = (
        ('featured', 'Featured'),
        ('trending', 'Trending'),
        ('breaking_story', 'Breaking Story'),
        ('top_story', 'Top Story'),
        ('developing', 'Developing'),
        ('normal', 'Normal'),
    )

    STORY_CATEGORY_CHOICES = (
        ('general', 'General'),
        ('social_news', 'Social News'),
        ('auto_news', 'Auto News'),
        ('technology', 'Technology'),
        ('business', 'Business'),
        ('education', 'Education'),
        ('health', 'Health'),
        ('life', 'Life'),
        ('sports', 'Sports'),
        ('crime', 'Crime'),
        ('cryptocurrency', 'Cryptocurrency'),
        ('entertainment', 'Entertainment'),
        ('national', 'National'),
        ('politics', 'Politics'),
        ('climate', 'Climate'),
        ('science', 'Science'),
        ('world', 'World'),
        ('videos', 'Videos')

    )

    MEDIA_TYPE_CHOICES = (
        ('broadcast', 'Broadcast'),
        ('internet', 'Internet'),
        ('magazine', 'Magazine'),
        ('newspaper', 'Newspaper'),
        ('press-agency','Press Agency'),
        ('news', 'News'),


    )

    title = models.CharField(max_length=500)
    link=models.URLField()
    slug = models.SlugField(max_length=500,
                            unique_for_date='publish', null=True, blank=True)
    media_house = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(max_length=600, null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    developing = models.BooleanField(default=False)
    image=models.URLField(null=True, blank=True)
    media_type=models.CharField(max_length=500, choices=MEDIA_TYPE_CHOICES, default='news')
    updated = models.DateTimeField(auto_now=True)
    continent = models.CharField(max_length=50, null=True, blank=True)
    subregion = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    guid = models.CharField(max_length=50)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='published')

    story_category = models.CharField(max_length=100, choices=STORY_CATEGORY_CHOICES, default='general')
    story_type = models.CharField(max_length=100, choices=STORY_TYPE_CHOICES, default='normal')


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

