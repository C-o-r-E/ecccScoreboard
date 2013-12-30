from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from scoreboard.models import Team, Score


def all_scores(request):
    teams = Team.objects.order_by('-team_score')

    return render_to_response(
        'scoreboard/scores.html',
        {'teams' : teams},
        context_instance = RequestContext(request)
    )
        
def team_scores(request, t_name):
    selected_team = Team.objects.get(name=t_name)
    scores = Score.objects.filter(team=selected_team.id)

    return render_to_response(
        'scoreboard/team_score.html',
        {'team' : selected_team,
         'scores' : scores },
        context_instance = RequestContext(request)
    )
