from django.shortcuts import redirect, render
from django.contrib.auth import logout,authenticate, login
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    if request.method=="POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
    return render(request, 'schoolquiz/index.html')

def register(request):
    if request.method=="POST":
        print("here")
        is_teacher=False
        is_student=False
        print(request.POST)
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        email = request.POST.get('email','')
        frist_name = request.POST.get('frist_name','')
        last_name = request.POST.get('last_name','')
        mobile = request.POST.get('mobile','')
        print(mobile,type(mobile), username)
        if request.POST.get('type')=='teacher':
            is_teacher = True
        else:
            is_student = True 
        user = User.objects.create_user(username,email,password)
        user.frist_name = frist_name
        user.last_name = last_name
        user.mobile = mobile
        user.is_teacher = is_teacher
        user.is_student = is_student
        user.save()
        return redirect('/')
    return render(request, 'schoolquiz/register.html')

def dashboard(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        quiz = Quiz(name=name,createdby=request.user,createdon=datetime.today())
        quiz.save()
        return redirect('/dashboard')

    if request.user:
        if request.user.is_teacher:
            quizes = Quiz.objects.all()
            return render(request, 'schoolquiz/dashboard.html', {"quiz":quizes})
        elif request.user.is_student:
            quizes = Quiz.objects.all()
            return render(request,'schoolquiz/sdashboard.html', {"quiz":quizes})
        
    return redirect('/')

def addquestion(request):
    query = Quiz.objects.get(name=request.GET['name'],createdby=User.objects.get(username=request.GET['by']))
    if request.method=="POST":
        question = request.POST.get('question','')
        option1 = request.POST.get('option1','')
        option2 = request.POST.get('option2','')
        option3 = request.POST.get('option3','')
        option4 = request.POST.get('option4','')
        answer = request.POST.get('answer','')
        question = Questions(question=question,option1=option1,option2=option2,option3=option3,option4=option4,answer=answer,relatedquiz=query)
        question.save()
    questions = Questions.objects.filter(relatedquiz=query)
    return render(request, "schoolquiz/addquestions.html",{"data":request.GET,"questions":questions})

def take_quiz(request):
    query = Quiz.objects.get(name=request.GET['name'],createdby=User.objects.get(username=request.GET['by']))
    questions = Questions.objects.filter(relatedquiz=query)
    if request.method=="POST":
        question = request.POST.get('question','')
        option1 = request.POST.get('option1','')
        option2 = request.POST.get('option2','')
        option3 = request.POST.get('option3','')
        option4 = request.POST.get('option4','')
        # print(question,option4,option1,option2,option3)
        if option1:
            answer = option1
        elif option2:
            answer = option2
        elif option3:
            answer = option3
        else:
            answer = option4
        
        que = Questions.objects.get(relatedquiz=query,question=question)
        if answer==que.answer:
            correct = True
        else:
            correct = False
        ans = Answer(quiz=query,question=que,answer=answer, correct=correct, student=request.user)
        ans.save()

    return render(request, "schoolquiz/ansquestions.html",{"data":request.GET,"questions":questions, "name":request.GET['name'], "by":request.GET['by']})

def result(request):
    print(request.GET['name'])
    query = Answer.objects.filter(quiz=Quiz.objects.get(name=request.GET['name'],createdby=User.objects.get(username=request.GET['by'])),student=request.user)
    query2 = Answer.objects.filter(quiz=Quiz.objects.get(name=request.GET['name'],createdby=User.objects.get(username=request.GET['by'])),correct=True,student=request.user)
    return render(request,"schoolquiz/result.html",{"obtained":len(query2),"total":len(query)})

def logout_view(request):
    logout(request)
    return redirect('/')