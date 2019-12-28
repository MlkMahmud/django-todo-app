from django.db import models

class Todo(models.Model):
  task = models.CharField(max_length=100)
  pub_date = models.DateTimeField("date published")
  def __str__(self):
    return self.task
