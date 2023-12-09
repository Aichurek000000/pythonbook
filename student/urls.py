from django.urls import path, include
from .views import *
from student.serializers import *
from rest_framework import routers

app_name = 'student'

router = routers.DefaultRouter()
# router.register(r'student-viewset', StudentViewset)
urlpatterns = [

    path('list-generic/', StudentsGenericView.as_view(), name='list-generic'),
    #path('student-set/', include(router.urls)),
    path('detail/<int:pk>/', StudentDetailAPIView.as_view(), name="student-detail"),
    path('list/', StudentsView.as_view(), name="list"),
    path('list-generic-update/', StudentsGenericUpdateView.as_view(), name='list-generic'),
    path('list-generic-destroy/', StudentsGenericDestroyView.as_view(), name='list-generic'),
    path('list-generic-create/', StudentsGenericCreateView.as_view(), name='list-generic'),
    path('list-generic/', StudentsGenericView.as_view(), name='list-generic')
]
