from django.conf.urls import patterns, url

from scoreboard import views

urlpatterns = patterns('',
                       url(r'^$', views.all_scores, name='score_list'),
)
