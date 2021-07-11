from datetime import datetime, timedelta
from django.test import TestCase
from django.utils import timezone
from .models import Quiz_Model


# Create your tests here.

class Quiz_Model_Test(TestCase):
  def test_on_going_quiz(self):
    time = timezone.now()
    quiz = Quiz_Model(end_date = time)
    self.assertIs(quiz.on_going_quiz(), True)
  
  def test_on_going_quiz_less_time(self):
    time = timezone.now() + timedelta(minutes=-1)
    quiz = Quiz_Model(end_date = time)
    self.assertEqual(quiz.on_going_quiz(), False)

  def test_ongoing_plus_time(self):
    time = timezone.now() + timedelta(days=-1)
    quiz = Quiz_Model(end_date = time)
    self.assertEqual(quiz.on_going_quiz(), False)
  
  def test_on_previous_quiz(self):
    time = timezone.now()
    quiz = Quiz_Model(end_date = time)
    self.assertIs(quiz.previous_quiz(), False)
  
  def test_previous_less_time(self):
    time = timezone.now() + timedelta(minutes=-1)
    quiz = Quiz_Model(end_date = time)
    self.assertEqual(quiz.previous_quiz(), True)

  def test_previous_plus_time(self):
    time = timezone.now() + timedelta(days=-1)
    quiz = Quiz_Model(end_date = time)
    self.assertEqual(quiz.previous_quiz(), True)
  
  def test_upcoming_quiz(self):
    time = timezone.now()
    quiz = Quiz_Model(start_date = time)
    self.assertIs(quiz.up_coming_quiz(), False)
  
  def test_upcoming_less_time(self):
    time = timezone.now() + timedelta(minutes=+1)
    quiz = Quiz_Model(start_date = time)
    self.assertEqual(quiz.up_coming_quiz(), True)

  def test_upcoming_plus_time(self):
    time = timezone.now() + timedelta(days=-1)
    quiz = Quiz_Model(start_date = time)
    self.assertEqual(quiz.up_coming_quiz(), False)
