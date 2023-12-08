from rest_framework.views import APIView
from rest_framework.response import Response
from task.models import *
from task.serializers import *


class TaskDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        task_object = Task.objects.get(pk=kwargs.get("pk"))
        serializer = TaskSerializer(instance=task_object)
        return Response(serializer.data)

    def put(sdelf, request, *args, **kwargs):
        task_object= Task.objects.get(pk=kwargs.get("pk"))

        serializer = TaskUpdateSerializer(
            instance=task_object,
            data=request.data
        )
        if serializer.is_valid():
            task_object=serializer.save()
            return Response(serializer.data, 202)
        else:
            return Response(serializer.errors, 400)

    def delete(sdelf, request, *args, **kwargs):
        task_object= Task.objects.get(pk=kwargs.get("pk"))  
        task_object.delete()
        return Response("deleted", 204)    


class TasksView(APIView):
    def get(self, request, *args, **kwargs):
        task_list = Task.objects.all()
        serializer = TaskSerializer(task_list, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        request_data = request.data
        serializer = TaskCreateSerializer(data=request_data)
        if serializer.is_valid():
            new_task = serializer.save()
            return Response("Успешно создано", 201)
        else:
            return Response(serializer.error_messages, 400)
        
class AnswersView(APIView):
    def get(self, request, *args, **kwargs):
        answer_list = Answer.objects.all()
        serializer = AnswerSerializer(answer_list, many=True)
        return Response(serializer.data)
    
class AnswerDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        answer_object = Answer.objects.get(pk=kwargs.get("pk"))
        serializer = AnswerSerializer(instance=answer_object)
        return Response(serializer.data)
    
    def put(sdelf, request, *args, **kwargs):
        answer_object= Answer.objects.get(pk=kwargs.get("pk"))

        serializer = AnswerSerializer(
            instance=answer_object,
            data=request.data
        )
        if serializer.is_valid():
            answer_object=serializer.save()
            return Response(serializer.data, 202)
        else:
            return Response(serializer.errors, 400)
    
    def delete(sdelf, request, *args, **kwargs):
        answer_object= Answer.objects.get(pk=kwargs.get("pk"))  
        answer_object.delete()
    


        
