from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView, RetrieveAPIView
from .serializers import *

# Create your views here.

class StudentDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        task_object = Student.objects.get(pk=kwargs.get("pk"))
        serializer = StudentsSerializer(instance=task_object)
        return Response(serializer.data)
    def put(self, request, *args, **kwargs):
        student_object= Student.objects.get(pk=kwargs.get("pk"))

        serializer = StudentsUpdateSerializer(
            instance=student_object,
            data=request.data
        )
        if serializer.is_valid():
            student_object=serializer.save()
            return Response(serializer.data, 202)
        else:
            return Response(serializer.errors, 400)

    def delete(self, request, *args, **kwargs):
        student_object= Student.objects.get(pk=kwargs.get("pk"))  
        student_object.delete()
        return Response("deleted", 204)   
    
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
        student_list = Student.objects.all()
        serializer = StudentsSerializer(student_list, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        request_data = request.data
        serializer = StudentsCreateSerializer(data=request_data)
        if serializer.is_valid():
            new_student = serializer.save()
            return Response("Успешно создано", 201)
        else:
            return Response(serializer.error_messages, 400)
        


class StudentsGenericView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class StudentsGenericUpdateView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class StudentsGenericDestroyView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


class StudentsGenericListView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class StudentsGenericRetriveView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class StudentsGenericCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class StudentGenericDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

        



        
        
   
        
        


