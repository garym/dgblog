from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import Post


class LatestEntriesFeed(Feed):
    title = "Recent blog posts"
    link = "/feeds/"
    description = "Recent blog posts."

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        text = item.text
        length = 140

        if len(text) > length:
            words = text[:length - 1].split()[:-1]
            if words:
                return ' '.join(words) + '…'
            return text[:length - 2] + ' …'

        return text

    # item_link is only
    # needed if NewsItem has
    # no get_absolute_url
    # method.
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
