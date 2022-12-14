from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    title = "Это главная страница проекта Yatube"
    context = {'title': title}
    return render(request, 'sema/index.html', context)


def group_list(request):
    title = "Здесь будет информация о группах проекта Yatube"
    context = {'title': title}
    return render(request, 'sema/group_list.html', context)


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1>{catid}</p>")