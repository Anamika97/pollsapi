from rest_framework import serializers

from .models import Poll, Choice, Vote
from django.contrib.auth.models import User


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many = True, read_only=True, required = False)
    question = serializers.SerializerMethodField()
    
    def get_question(self, obj):
        return obj.poll.question
        
    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many = True, read_only = True, required = False)
    username = serializers.SerializerMethodField()
    user = UserSerializer(read_only = True)

    def get_username(self, obj):
        return obj.created_by.username

    class Meta:
        model = Poll
        fields = '__all__'
