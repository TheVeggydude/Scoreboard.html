from django.shortcuts import render
from .models import Team, Exercise
import django_tables2 as tables


class TeamTable(tables.Table):
    class Meta:
        model = Team
        fields = ('name', 'score', 'beers')
        attrs = {"class": "table"}
        empty_text = "No teams available"


def index(request):
    teams = Team.objects.all()
    teams_table = TeamTable(teams, prefix='teams-')
    tables.config.RequestConfig(request).configure(teams_table)

    return render(request, 'scoreboard/index.html', {'teams_table': teams_table})


class ExerciseTable(tables.Table):
    class Meta:
        model = Exercise
        fields = {'text'}
        attrs = {"class": "table"}
        empty_text = "No assignments available"


def exercises(request):
    exercises = Exercise.objects.all().filter(available=True)
    exercise_table = ExerciseTable(exercises, prefix='exercise-')
    tables.config.RequestConfig(request).configure(exercise_table)

    return render(request, 'scoreboard/exercises.html', {'exercise_table': exercise_table})
