from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('register', views.register, name='register'),
    path('register_user', views.register_user, name='register_user'),
    path('quiz', views.quiz_home, name='quiz'),
    path('college_admin', views.admin, name='college_admin'),
    path('college_home', views.college_home, name='college_home'),
    path('add_quiz', views.add_quiz, name='add_quiz'),
    path('start_quiz/<int:id>/<int:s_id>/', views.start_quiz, name='start_quiz'),
    path('quiz/<int:q_id>/<int:s_id>/result', views.quiz_result, name='result'),
    path('college-admin/std-results', views.student_results, name='std-result'),
]