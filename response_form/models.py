#response_form/models.py

import sys
sys.path.insert(0,'..')

from django.db import models
from django.conf import settings
import questions_and_answers


class ResponseModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    q1 = models.CharField(max_length=200)
    q2 = models.CharField(max_length=200)
    text = models.TextField()
    title = models.CharField(max_length=200, default='user') #redundant
    submit_count = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title
