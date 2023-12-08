from django.urls import path, include
from .views.task import *

app_name = "answer"

urlpatterns = [
    path('detail/<int:pk>/', AnswerDetailAPIView.as_view(), name="answer-detail"),
    path('list/', AnswersView.as_view(), name='list'),
]