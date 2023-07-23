import sys

from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

import toml

from main.models import Class, Assessment


def rankings() -> dict[int, list]:
    rankings = {}
    class_levels = sorted(set([int(str(x)[:-1]) for x in Class.objects.all()]))
    
    for level in class_levels:
        parallel_classes = Class.objects.filter(class_name__contains=level)
        rankings[level] = list()
        
        for _class in parallel_classes:
            score = Assessment.objects.filter(class_name=_class).aggregate(Sum('score'))['score__sum']
            score = score if score else 0
            
            rankings[level].append({'class': str(_class), 'score': score})

    # Sort rankings ascending by class level and descending by score
    rankings = dict((k, sorted(v, key=lambda x: x['score'],
                               reverse=True),) for k, v in
                    sorted(rankings.items()))

    for level, classes in rankings.copy().items():
        previous_ranking = 0
        previous_score = sys.maxsize

        for key, value in enumerate(classes):
            current_score = value['score']

            if previous_score == current_score:
                current_ranking = previous_ranking
            else:
                current_ranking = previous_ranking + 1

            rankings[level][key]['ranking'] = current_ranking
            previous_ranking = current_ranking
            previous_score = current_score

    return rankings


def load_configuration() -> dict:
    with open('config.toml', 'r') as f:
        return toml.load(f)


def index(request: HttpRequest) -> HttpResponse:
    context = {'scores': rankings(), 'config': load_configuration()}
    return render(request, 'main/index.html', context)


def scoreboard(request: HttpRequest) -> HttpResponse:
    context = {'scores': rankings(), 'config': load_configuration(), 'autoscroll': True}
    return render(request, 'main/index.html', context)

def scoreboard_with_autoreload(request: HttpRequest) -> HttpResponse:
    context = {'scores': rankings(), 'config': load_configuration(), 'autoscroll': True, 'autoreload': True}
    return render(request, 'main/index.html', context)
