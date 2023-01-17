from django.shortcuts import render
from django.http import HttpResponse,HttpRequest, HttpResponseRedirect
from quizapp.models import QQuestion,Answer
from django.urls import reverse

# Create your views here.
def home(request):
    question = QQuestion.objects.all()
    print(question)
    answer = Answer.objects.all()
    context = {"questions":question,"answers":answer}
    return render(request,"home.html",context)


def result(request):
    answer_users = request.POST.getlist('answer_user')
    print(answer_users)
    answers = Answer.objects.all()
    print(answers)
    questions = QQuestion.objects.all()
    print(questions)
    # print(answer)
    # marks_count = 0
    # for ans in answer_user:
    #     if ans == 
    answer_right = []
    for answer in answers:
        if answer.is_correct == True:
            answer_right.append(answer.title)
            
    print("Right answer is: ",answer_right)        
         
    marks_count = 0
    # ans = filter(answer_users,answer_right)
    for answer_user in answer_users:
        for answer_r in answer_right:
            if answer_user == answer_r:
                print(answer_user)
                marks_count = marks_count + 1
            
        
    print(marks_count)    
                    
    context = {"marks_count":marks_count}        
    return render(request,"result.html",context)


    
