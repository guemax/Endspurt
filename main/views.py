from datetime import datetime
import sys

from django.db.models import Sum, Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from main.models import Class, Station, Assessment


def index(request: HttpRequest) -> HttpResponse:
    scores = {}
    
    # Get class levels
    classes = Class.objects.all()
    class_levels = sorted(set([x.class_level for x in classes]))
    print(class_levels)

    for level in class_levels:
        # Get parallel_classes
        classes = Class.objects.filter(class_level=level).order_by('class_level', 'parallel_class')
        print(classes)

        scores_for_parallel_classes = []

        for parallel_class in classes:
            # Get total score
            score = Assessment.objects.filter(class_name=parallel_class).aggregate(total=Sum('score'))['total']

            if score is None:
                score = 0
                
            print(score)

            scores_for_parallel_classes.append({'class': str(parallel_class), 'score': score})

        scores_for_parallel_classes = sorted(scores_for_parallel_classes, key=lambda x: x['score'], reverse=True)

        # Calculate rankings
        previous_score = sys.maxsize
        previous_ranking = 0

        for key, score in enumerate(scores_for_parallel_classes):
            print(f'{score["class"]} with {score["score"]} points, previously {previous_score} point. Previous ranking: {previous_ranking}')
            if score['score'] == previous_score:
                print("Do not increment ranking")
                score['ranking'] = previous_ranking
            else:
                current_ranking = previous_ranking + 1
                score['ranking'] = current_ranking
                previous_ranking = current_ranking

            previous_score = score['score']
            scores_for_parallel_classes[key] = score
                

        scores[level] = sorted(scores_for_parallel_classes, key=lambda x: x['ranking'])

    print(scores)
    context = {'scores': scores}
    return render(request, 'main/index.html', context)
