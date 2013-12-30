from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from scoreboard.models import Team


def all_scores(request):
    teams = Team.objects.order_by('-team_score')

    return render_to_response(
        'scoreboard/scores.html',
        {'teams' : teams},
        context_instance = RequestContext(request)
    )
        
