from django.db import models


class Question(models.Model):
    subject = models.CharFteld(max_length=200)
    content = models.TextField()
    create_date = models.DateTimField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimField()

