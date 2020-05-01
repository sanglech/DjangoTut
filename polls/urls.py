from django.conf.urls import include
from django.urls import path
from . import views

app_name='polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/ - Look at question 5
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/ results for question 5
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/ vote for question 5
    path('<int:question_id>/vote/', views.vote, name='vote'),
]