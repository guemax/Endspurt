from django.urls import path

from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('anzeigetafel/', views.scoreboard, name='scoreboard'),
    path('anzeigetafel/automatisches-nachladen/',
         views.scoreboard_with_autoreload,
         name='scoreboard_with_autoreload'
         ),
]
