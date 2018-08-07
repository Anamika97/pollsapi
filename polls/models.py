from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length = 100)
    created_by = models.ForeignKey(User, default=1)
    pub_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, related_name = 'choices')
    choice_text = models.CharField(max_length = 100)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice, related_name = 'votes')
    voted_by = models.ForeignKey(User)

    class Meta:
        unique_together = ("poll", "voted_by")

    def __str__(self):
        return str(self.poll) + ' --> ' + str(self.choice)
