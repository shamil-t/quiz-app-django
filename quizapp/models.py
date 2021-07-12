from django.db import models
from datetime import datetime
from django.utils import timezone
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

  def on_going_quiz(self):
    if self.end_date >= timezone.now() and self.start_date <= timezone.now():
      return True
    else :
      return False

  def up_coming_quiz(self):
    if self.start_date > timezone.now() :
      return True
    else :
      return False
  
  def previous_quiz(self):
    if self.end_date < timezone.now() :
      return True
    else :
      return False

  def __str__(self):
      return str(self.id)

class Quiz_result(models.Model):
  quiz_type = models.IntegerField(default=0)
  s_id = models.IntegerField(default=0)
  result = models.IntegerField(default=0)

  def get_all_results(self):
    User = User_Model.objects.get(id = self.s_id)
    s_name = User.user_name
    reg_no = User.reg_no
    q_name = Quiz_Model.objects.get(id = self.quiz_type).quiz_name

    result = {
      'name':s_name,
      'reg_no':reg_no,
      'quiz':q_name,
      'result':self.result
    }

    return result


  def __str__(self):
      return str(self.result)
  
  