from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
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
