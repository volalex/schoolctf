from django.http.response import HttpResponseNotFound
from django.shortcuts import render

#registration view
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from schoolctf.forms import RegistrationForm
from scoreboard.models import News, Task


def index(request):
    if request.method == "GET":
        return TemplateResponse(request, "index.html")
    else:
        return HttpResponseNotFound


def tasks(request):
    return TemplateResponse(request, "tasks_main.html")


def task_detail(request, task_pk):
    try:
        task = Task.objects.get(pk=task_pk)
        return TemplateResponse(request, "tasks_detail.html", task)
    except Task.DoesNotExist:
        return HttpResponseNotFound("Not found")


@never_cache
@csrf_protect
@sensitive_post_parameters
def task_solve(request, task_pk):
    if request.method == "POST":
        pass
    else:
        return HttpResponseNotFound("Not Found")


def detail_news(request, pk):
    return TemplateResponse(request, "article.html", context={"article": News.objects.get(pk=pk), "news_pk": pk})


@sensitive_post_parameters()
@csrf_protect
@never_cache
def registration(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return TemplateResponse(request, "registration/registration_success.html")
    else:
        context = {
            'form': RegistrationForm(),
        }
    return TemplateResponse(request, "registration/reg_form.html", context)