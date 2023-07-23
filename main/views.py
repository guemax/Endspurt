import sys

from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from main.models import Class, Assessment


def rankings() -> dict[str, list]:
    rankings = {}
    
    for level in sorted(set([int(str(x)[:-1]) for x in Class.objects.all()])):
        parallel_classes = Class.objects.filter(class_name__contains=level)
        rankings[level] = list()

        for class_ in parallel_classes:
            score = Assessment.objects.filter(class_name=class_).aggregate(Sum('score'))['score__sum']

            if score is None:
                score = 0

            rankings[level].append({'class': str(class_), 'score': score})

    # Sort rankings ascending by class level and descending by score
    rankings = dict((k, sorted(v, key=lambda x: x['score'],
                               reverse=True),) for k, v in
                    sorted(rankings.items()))

    for k, v in rankings.copy().items():
        previous_ranking = 0
        previous_score = sys.maxsize

        for i, j in enumerate(v):
            current_score = j['score']

            if previous_score == current_score:
                current_ranking = previous_ranking
            else:
                current_ranking = previous_ranking + 1

            rankings[k][i]['ranking'] = current_ranking
            previous_ranking = current_ranking
            previous_score = current_score

    return rankings


def index(request: HttpRequest) -> HttpResponse:
    context = {'scores': rankings()}
    return render(request, 'main/index.html', context)


def scoreboard(request: HttpRequest) -> HttpResponse:
    context = {'scores': rankings(), 'autoscroll': True}
    return render(request, 'main/index.html', context)

def scoreboard_with_autoreload(request: HttpRequest) -> HttpResponse:
    context = {'scores': rankings(), 'autoscroll': True, 'autoreload': True}
    return render(request, 'main/index.html', context)
