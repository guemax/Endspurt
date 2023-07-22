from datetime import datetime
import sys

from django.db.models import Sum
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from main.models import Class, Station, Assessment


def get_class_levels() -> list[int]:
    return sorted(set([x.class_level for x in Class.objects.all()]))


def get_parallel_classes(level: int) -> QuerySet:
    return Class.objects.filter(
        class_level=level
    ).order_by(
        'class_level',
        'parallel_class'
    )


def get_total_score(parallel_class: Class) -> int:
    score = Assessment.objects.filter(
        class_name=parallel_class
    ).aggregate(
        total=Sum('score')
    )['total']

    # Score can be None when there are no
    # assessments for this parallel class
    if score is None:
        return 0

    return score


def get_scores() -> dict[list]:
    scores = {}

    for level in get_class_levels():
        scores_for_level = []

        for parallel_class in get_parallel_classes(level):
            score = get_total_score(parallel_class)
            scores_for_level.append({'name': str(parallel_class), 'score': score})

        # Sort scores for class level descending by score
        scores_for_level = sorted(
            scores_for_level,
            key=lambda x: x['score'],
            reverse=True
        )

        previous_score = sys.maxsize
        previous_ranking = 0

        for key, parallel_class in enumerate(scores_for_level):
            if parallel_class['score'] == previous_score:
                parallel_class['ranking'] = previous_ranking
            else:
                current_ranking = previous_ranking + 1
                parallel_class['ranking'] = current_ranking
                previous_ranking = current_ranking

            previous_score = parallel_class['score']
            scores_for_level[key] = parallel_class

        # Sort scores ascending by ranking
        scores[level] = sorted(
            scores_for_level,
            key=lambda x: x['ranking']
        )

    return scores


def index(request: HttpRequest) -> HttpResponse:
    context = {'scores': get_scores(), 'autoscroll': False}
    return render(request, 'main/index.html', context)


def scoreboard(request: HttpRequest) -> HttpResponse:
    context = {'scores': get_scores(), 'autoscroll': True}
    return render(request, 'main/index.html', context)
