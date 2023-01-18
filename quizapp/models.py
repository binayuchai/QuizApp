from django.db import models
from django.conf import settings
# Create your models here.

class TimeStampModal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        abstract = True
     


class Category(TimeStampModal):
    category = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category    
    
    
    
    
class QQuestion(TimeStampModal):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
        
   
 
class Answer(TimeStampModal):
    title = models.CharField(max_length=250)
    question = models.ForeignKey(QQuestion, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return self.title
    
# class Progress(TimeStampModal):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="progress_user")
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     is_started = models.BooleanField(default=False)
#     is_completed = models.BooleanField(default=False)
    
    
    
    
# class Result(TimeStampModal):
#     score = models.CharField(max_length=200)
#     player = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="result")
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     is_completed = models.BooleanField(default=False)
                  
    
    

    


    