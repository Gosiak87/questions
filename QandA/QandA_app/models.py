from django.db import models

# Create your models here.


class Question(models.Model):
    TECHNOLOGY = (
        (-1, "undefined"),
        (1, "Python"),
        (2, "Java Script"),
        (3, "Linux"),
        (4, "HTML"),
        (5, "CSS")
    )
    content = models.CharField(max_length=300)
    answer = models.CharField(max_length=1000, null=True, blank=True)
    technology = models.IntegerField(choices=TECHNOLOGY, default=-1)
