from django.shortcuts import render
from django.views.generic import View,TemplateView, DetailView ##새로추가
from django.http import HttpResponse ## 새로추가

from .models import School

# Create your views here.

def index(request):
    return render(request,'posts/index.html')

class CBView(View):
    def get(self, request):
        return HttpResponse("실행완료!!!")
    
class IndexView(TemplateView):
    template_name = 'posts/cbv_index.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting'] = "안녕하세요!!"
        return context
        
        
class SchoolDetailView(DetailView):
    model = School
    template_name = 'posts/school_detail.html'
