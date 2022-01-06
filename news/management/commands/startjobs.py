# podcasts/management/commands/startjobs.py
from news.feeds import cnn
from django.core.management.base import BaseCommand
from news.feeds import cnn
import feedparser

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from news.models import Post


def save_new_media_house(feed, media_house,image, story_category, country, continent,subregion,media_type):
    """Saves new episodes to the database.

    Checks the episode GUID against the episodes currently stored in the
    database. If not found, then a new `Episode` is added to the database.

    Args:
        feed: requires a feedparser object
    """
    # media_title = feed.channel.title

    for item in feed.entries:
        if not Post.objects.filter(guid=item.guid).exists():
            episode = Post(
                title=item.title,
                link=item.link,
                #From here I put the details personally
                media_house=media_house,
                image=image,
                story_category= story_category,
                country=country,
                continent=continent,
                subregion=subregion,
                media_type=media_type,
                guid=item.guid,
            )
            episode.save()


def fetch_nation():
    """Fetches new episodes from RSS for the Talk Python to Me Podcast."""

    _feed = feedparser.parse("https://rss.app/feeds/sPBEmYOM5jBOba2w.xml")
    save_new_media_house(_feed, 'Nation Media Group','https://yt3.ggpht.com/ytc/AKedOLS6Li6K0CQ3vjr6xF8tzfCyAgCo8CaL_X70wKRv8A=s900-c-k-c0x00ffffff-no-rj', 'national','kenya','africa', 'eastern africa','newspaper')


def fetch_star():
    _feed = feedparser.parse("https://www.the-star.co.ke/rss")
    save_new_media_house(_feed, 'The Star','https://www.the-star.co.ke/publication/custom/static/logos/logo.the-star.png','general', 'kenya', 'africa', 'eastern africa','newspaper')


def fetch_standard_media():
    _feeds=['https://www.standardmedia.co.ke/rss/headlines.php', 'https://www.standardmedia.co.ke/rss/kenya.php', 'https://www.standardmedia.co.ke/rss/world.php']
    for _feed in _feeds:
        standardlink= feedparser.parse(_feed)
        save_new_media_house(standardlink, 'Standard Media Group', 'https://pbs.twimg.com/profile_images/832503365594705920/9Vg7GYdf_400x400.jpg','general', 'kenya', 'africa', 'eastern africa','newspaper' )



class Command(BaseCommand):
    def handle(self, *args, **options):
        fetch_nation()
        fetch_star()
        fetch_standard_media()
