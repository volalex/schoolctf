from django import template
from scoreboard.models import News, SolvedTasks

__author__ = 'volal_000'

register = template.Library()


@register.inclusion_tag("includes/news.html")
def news_block(news_pk):
    try:
        news = News.objects.all().order_by('create_date').reverse()[:5]
    except News.DoesNotExist:
        news = []
    return {"news_list": news, "active_pk": news_pk}


@register.inclusion_tag("includes/results.html")
def results():
    return {}
