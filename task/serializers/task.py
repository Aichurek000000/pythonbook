from rest_framework import serializers
from users.serializers import UserSerializer
from django.contrib.auth.models import User
from task.models.task import *

class TaskSerializer(serializers.ModelSerializer):
    view_by =UserSerializer(many=True, read_only=True)
    view_count = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ['name', 'description', 'view_by', 'view_count']
    def get_view_count(self, task_obj):
        return task_obj.view_by.count()

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description','difficulty']

class TaskAddViewSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='views_by.id')
    
    class Meta:
        model = Task
        fields = ['user_id']
    
    def update(self, instance, validated_data):
        user_id = validated_data.get('user_id')
        user_object = User.objects.get(id=user_id)
        instance.views_by.add(user_object)
        return instance
    
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['txt',]