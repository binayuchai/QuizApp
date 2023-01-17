from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from quizapp.models import QQuestion,Answer

# Create your views here.
def home(request):
    question = QQuestion.objects.all()
    answer = Answer.objects.all()
    context = {"questions":question,"answers":answer}
    return render(request,"home.html",context)


def result(request):
    answer = request.POST.getlist('answer.title[]') 
    print(answer)
    return HttpResponse("Clicked")