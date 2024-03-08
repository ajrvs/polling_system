from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text