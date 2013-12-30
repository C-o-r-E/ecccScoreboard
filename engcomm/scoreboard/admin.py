from django.contrib import admin

from scoreboard.models import Team, Competition, Score

admin.site.register(Team)
admin.site.register(Competition)
admin.site.register(Score)


