from django.db import models
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name = models.CharField(max_length= 100)
    location =  models.CharField(max_length= 100)
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self): #리다이렉트 주소설정하는 메소드
        return reverse('posts:list')
    
class Student(models.Model):
    name =  models.CharField(max_length= 100)
    age = models.PositiveIntegerField()
    
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    