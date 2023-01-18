from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from quizapp.models import QQuestion,Answer, Category

# Create your views here.
def home(request):
    questions = QQuestion.objects.all()
    categories = Category.objects.all()
    answers = Answer.objects.all()
    context = {"questions":questions,"answers":answers,"categories":categories}
    return render(request,"home.html",context)


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
                
            
            
    print(marks_count)      
    context = {"marks":marks_count}  
    Progress.is_completed = True
            
    return render(request,"result.html",context)



def q_question(request,categoryid):
    categories = Category.objects.get(id=categoryid)
    questions = QQuestion.objects.filter(category=categories)
    answers = Answer.objects.all()
    context = {"questions":questions,"answers":answers,"categories":categories}

    # obj,created = Progress.objects.get_or_create(
    #     is_started = True,
    #     is_completed = False,
    #     defaults={
    #         "progress_categories":categories,
    #         "progress_questions":questions,
    #         "progress_answers":answers,
    #     }
                    
            
    #     )
    
    return render(request,"question.html",context)

# def progress(request):
#         pass

    
        


    