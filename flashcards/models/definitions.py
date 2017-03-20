from django.db import models


class Word(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=24)
    wordclass = models.CharField(max_length=24)

    class Meta:
        unique_together = ('word', 'wordclass')



