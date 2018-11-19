from . import views
from django.urls import path


app_name = 'posts'

urlpatterns = [
    path('',views.index,name='index'),
    path('cbv/',views.CBView.as_view()),
    path('cbv_index/',views.IndexView.as_view()),
    path('list/',views.SchoolListView.as_view(),name = 'list'),
    path('<int:pk>/',views.SchoolDetailView.as_view()), #url 요청이 들어오면 스쿨디테일뷰시작
    path('create/', views.SchoolCreateView.as_view()),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view()),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name = 'delete'),
]