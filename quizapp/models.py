from django.db import models
from datetime import datetime
# Create your models here.

class User_Model(models.Model):
  user_name = models.CharField(max_length=50)
  reg_no = models.IntegerField(default=0)
  pwd = models.CharField(max_length=13)

  def __str__(self):
      return self.user_name

class Quiz_Model(models.Model):
  quiz_name = models.CharField(max_length=100)
  quiz_type = models.IntegerField(default=0)
  start_date = models.DateTimeField()
  end_date = models.DateTimeField()

  def __str__(self):
      return str(self.quiz_type)

class Quiz_result(models.Model):
  quiz_type = models.IntegerField(default=0)
  s_id = models.IntegerField(default=0)
  result = models.IntegerField(default=0)

  def __str__(self):
      return str(self.result)
  
  