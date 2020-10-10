from django.db import models
from user.models import UserModel

# Create your models here.
class questions(models.Model):
    question_name = models.CharField(max_length=500)
    asked_by = models.ForeignKey(UserModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.question_name

class answers(models.Model):
    answer = models.CharField(max_length=1000)
    questions = models.ForeignKey(questions,on_delete=models.CASCADE)
