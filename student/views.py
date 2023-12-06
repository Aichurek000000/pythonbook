from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# Create your views here.

class StudentDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        task_object = Student.objects.get(pk=kwargs.get("pk"))
        serializer = StudentsSerializer(instance=task_object)
        return Response(serializer.data)
    
    # def post(self, request, *args, **kwargs):
    #     request_data = request.data
    #     serializer = StudentCreateSerializer(data=request_data)
    #     if serializer.is_valid():
    #         new_student = serializer.save()
    #         return Response("Успешно создано", 201)
    #     else:
    #         return Response(serializer.error_messages, 400)
        
class StudentsView(APIView):
    def get(self, request, *args, **kwargs):
        student_list = Task.objects.all()
        serializer = StudentsSerializer(student_list, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        request_data = request.data
        serializer = StudentCreateSerializer(data=request_data)
        if serializer.is_valid():
            new_student = serializer.save()
            return Response("Успешно создано", 201)
        else:
            return Response(serializer.error_messages, 400)

