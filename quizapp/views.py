from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from quizapp.models import QQuestion,Answer, Category, Progress, Result
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    questions = QQuestion.objects.all()
    categories = Category.objects.all()
    answers = Answer.objects.all()
    context = {"questions":questions,"answers":answers,"categories":categories}
    return render(request,"home.html",context)

@login_required(login_url="user:login")
def result(request):
    answer_users = request.POST.getlist('answer_user') 
    print(answer_users)
    answers = Answer.objects.all()
    questions = QQuestion.objects.all()
    right_answer = []
    for answer in answers:
        if answer.is_correct == True:
            right_answer.append(answer.title)
        
        
    print(right_answer)
    
    marks_count = 0
    for answer_user in answer_users:
        for answer in right_answer:
            if answer == answer_user:
                marks_count = marks_count + 1
                             
    category_result = request.POST.get('result_category')
    # print(question2)
    # question1 = QQuestion.objects.get(title=question2)
    # print(question1)
    # category = Category.objects.filter()
    result = Result(score=marks_count,player=request.user,category=Category.objects.get(category=category_result))
    result.save()
    
    context = {"marks":marks_count}  
    
            
    return render(request,"result.html",context)


@login_required(login_url="user:login")
def q_question(request,categoryid):

    categories = Category.objects.get(id=categoryid)
    questions = QQuestion.objects.filter(category=categories)
    answers = Answer.objects.all()
    print(categories)
   

    obj,created = Progress.objects.get_or_create(
        is_started = True,
        is_completed = False,
        player = request.user,
        category=categories,
        defaults={
            "category":categories,
            "is_started":True,
            "is_completed":False,
  
        }
                        
        )
    
    context = {"questions":questions,"answers":answers,"categories":categories}
    
    return render(request,"question.html",context)


@login_required(login_url="user:login")
def progress(request):
    progresses = Progress.objects.filter(is_started=True,is_completed=False, player=request.user)
    print(progresses)

    context = {"progresses":progresses}
    return render(request,"progress.html",context)
    
    
@login_required(login_url="user:login")    
def completed(request):
    results = Result.objects.filter(player=request.user)

    context={"results":results}
    return render(request,"completed.html",context)

        
    

    
        


    
