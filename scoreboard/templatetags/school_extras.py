from django import template
from django.db import connection
from django.db.models import Sum
from scoreboard.models import News, SolvedTasks, Team

__author__ = 'volal_000'

register = template.Library()


@register.inclusion_tag("includes/news.html")
def news_block(news_pk):
    try:
        news = News.objects.all().order_by('create_date').reverse()
    except News.DoesNotExist:
        news = []
    return {"news_list": news, "active_pk": news_pk}


@register.inclusion_tag("includes/results.html")
def results():
    teams = Team.objects.all().filter(is_admin=False)
    result_dict = {}
    for team in teams:
        solved_tasks = SolvedTasks.objects.all().filter(team=team)
        score = 0
        for solved_task in solved_tasks:
            score += solved_task.task.score
        result_dict[team] = score
    return {"results": result_dict}
