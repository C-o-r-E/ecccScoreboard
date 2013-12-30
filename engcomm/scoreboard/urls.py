from django.conf.urls import patterns, url

from scoreboard import views

urlpatterns = patterns('',
                       url(r'^$', views.all_scores, name='score_list'),
                       url(r'^team/(?P<t_name>\w+)$', views.team_scores, name='team_scores'),
)
