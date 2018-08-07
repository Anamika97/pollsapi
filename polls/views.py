from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import renderers

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Poll, Choice, Vote
from .forms import PollForm, ChoiceForm, VoteForm, UserForm
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


class PollsViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer, renderers.BrowsableAPIRenderer, renderers.JSONRenderer)

    def list(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            return Response({}, template_name='polls/polls.html')
        response = super(PollsViewSet, self).list(request, *args, **kwargs)
        return response


    def retrieve(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            return Response({}, template_name='polls/polls.html')
        response = super(PollsViewSet, self).retrieve(request, *args, **kwargs)
        return response

    def create(self, request, *args, **kwargs):
        form = PollForm(request.POST or None)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.question = form.cleaned_data.get('question')
            poll.created_by = request.user
            poll.save()
        return Response({}, template_name='polls/polls.html')
    

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer, renderers.BrowsableAPIRenderer, renderers.JSONRenderer)
    
    def list(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            return Response({}, template_name='polls/choices.html')
        response = super(ChoiceViewSet, self).list(request, *args, **kwargs)
        return response

    def retrieve(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            return Response({}, template_name='polls/choices.html')
        response = super(ChoiceViewSet, self).retrieve(request, *args, **kwargs)
        return response


    def create(self, request, *args, **kwargs):
        form = ChoiceForm(request.POST or None)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.poll = form.cleaned_data.get('poll')
            choice.choice_text = form.cleaned_data.get('choice_text')
            choice.save()
        return Response({}, template_name='polls/choices.html')
    

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer, renderers.BrowsableAPIRenderer,)
    
    def list(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'html':
            return Response({}, template_name='polls/votes.html')
        response = super(VoteViewSet, self).list(request, *args, **kwargs)
        return response

    def create(self, request, *args, **kwargs):
        form = VoteForm(request.POST or None)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.poll = form.cleaned_data.get('poll')
            vote.choice = form.cleaned_data.get('choice')
            vote.voted_by = request.user
            vote.save()
            print("vote recorded")
            
        return Response({}, template_name='polls/votes.html')


def login_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, 'polls/polls.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'polls/polls.html')

        else:
            return render(request, 'polls/login.html', {'error_message': 'Invalid login'})
    return render(request, 'polls/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'polls/login.html', {"form": form})