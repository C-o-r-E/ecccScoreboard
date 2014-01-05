from re import sub
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    uni = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    prov_state = models.CharField(max_length=255)
    team_score = models.IntegerField()

    def save(self, *args, **kwargs):
        self.name = sub(r'\s+', '_', self.name)
        super(Team, self).save(*args, **kwargs)

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
    notes = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        #get a list of all the other scores for team
        other_scores = Score.objects.filter(team=self.team).exclude(id=self.id)
        
        sum = self.score
        for s in other_scores:
            sum = sum + s.score

        self.team.team_score = sum
        self.team.save()
        
        super(Score, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s: %s -> %d" % (self.team.name, self.comp, self.score)
