from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    uni = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    prov_state = models.CharField(max_length=255)
    team_score = models.IntegerField()

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.uni)

class Competition(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s" % (self.name,)

class Score(models.Model):
    team = models.ForeignKey(Team)
    comp = models.ForeignKey(Competition)
    score = models.IntegerField()
    notes = models.TextField()

    def __unicode__(self):
        return u"%s: %s -> %d" % (self.team.name, self.comp, self.score)
