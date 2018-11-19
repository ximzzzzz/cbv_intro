from . import views
from django.urls import path


app_name = 'posts'

urlpatterns = [
    path('',views.index,name='index'),
    path('cbv/',views.CBView.as_view()),
    path('cbv_index/',views.IndexView.as_view()),
    path('<int:pk>/',views.SchoolDetailView.as_view()), #url 요청이 들어오면 스쿨디테일뷰시작
]