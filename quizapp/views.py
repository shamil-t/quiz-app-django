from django.core.checks import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import User_Model,Quiz_Model,Quiz_result

import requests
import random
from json import dumps


def home(request):

    return render(request, 'home.html')

def quiz_home(request):
    reg_no = request.POST['reg_no']
    pwd = request.POST['pwd']

    if User_Model.objects.filter(reg_no=reg_no).exists():
        User = User_Model.objects.get(reg_no=reg_no)
        print(User.reg_no, reg_no, User.pwd, pwd)
        pwd.strip()
        reg_no.strip()
        if User.pwd == pwd:
            name = User.user_name
            Quiz = Quiz_Model.objects.all()
            return render(request, 'quiz_home.html', {'name': name,'quiz':Quiz,'s_id':User.id})
        else:
            msg = 'Incorrect Password'
            return render(request, 'home.html', {'error': msg})
    else:
        msg = 'User Not Registered Please Register'
        return render(request, 'home.html', {'error': msg})

def register(request):

    return render(request, 'register.html')

def admin(request):

    return render(request, 'admin.html')

def register_user(request):
    u_name = request.POST['name']
    pwd = request.POST['pwd']
    reg_no = request.POST['reg_no']

    u_name.strip()
    reg_no.strip()
    pwd.strip()

    if User_Model.objects.filter(reg_no=reg_no).exists():
        return HttpResponse('User already Registered...!')
    else:
        user = User_Model(user_name=u_name, reg_no=reg_no, pwd=pwd)
        user.save()
        msg = 'User Registered Successfully, Now Login to your Account'
        return render(request, 'home.html', {'message': msg})

def college_home(request):
    pwd = request.POST['pwd']
    id = request.POST['id']

    if id == 'admin' and pwd == 'admin':
        return render(request, 'college.html')
    else:
        msg = ' Admin ID = "admin" and password = "admin" '
        return render(request, 'admin.html', {'message': msg})

def add_quiz(request):
  q_name = request.POST['q_name']
  id = request.POST['id']
  s_date = request.POST['s_date']
  e_date = request.POST['e_date']

  Quiz = Quiz_Model(quiz_name=q_name, quiz_type=id, start_date=s_date, end_date=e_date)
  Quiz.save()

  msg = 'Quiz Added Succesfully...!'
  return render(request, 'college.html',{'message':msg})

def start_quiz(request, id, s_id):

    Quiz = Quiz_Model.objects.get(quiz_type=id)
    title = Quiz.quiz_name

    url = 'https://opentdb.com/api.php?amount=10&category='+str(id)+'&difficulty=medium&type=multiple'
    data = requests.get(url)
    data_json = data.json()
    question_set = data_json['results']

    questions = []
    options = []
    answer = []

    for i in range( len(question_set)):
        questions.append(question_set[i]['question'])
        answer.append(question_set[i]['correct_answer'])
        option = question_set[i]['incorrect_answers']
        option.append(question_set[i]['correct_answer'])
        random.shuffle(option)
        options.append(option)

    DATA = {
        'questions': questions,
        'options': options,
        'answer' : answer
    }

    DATA_JSON = dumps(DATA)

    return render(request, 'start_quiz.html', {'data': DATA_JSON, 'title':title, 'id':id, 's_id':s_id})

def quiz_result(request, q_id, s_id):
    result = request.POST['result']
    time = request.POST['time']

    quiz = Quiz_result(quiz_type=q_id, s_id=s_id, result=result)
    quiz.save()

    Quiz_name = Quiz_Model.objects.get(quiz_type=q_id).quiz_name
    Std_name = User_Model.objects.get(id=s_id)

    return render(request, 'result.html', 
    {
        'result':result, 
        'q_name':Quiz_name,
        's_name':Std_name,
        'time':time
    })