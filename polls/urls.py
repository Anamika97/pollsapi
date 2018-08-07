from django.conf.urls import url, include

from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from .views import PollsViewSet, ChoiceViewSet, VoteViewSet
from polls import views

polls_list = PollsViewSet.as_view({
    'get': 'list'
})

polls_detail = PollsViewSet.as_view({
    'get': 'retrieve'
})

choice_list = PollsViewSet.as_view({
    'get': 'list'
})

choice_create = PollsViewSet.as_view({
    'post': 'create'
})

vote_create = VoteViewSet.as_view({
    'post': 'create'
})

router = DefaultRouter()
router.register(r'polls', views.PollsViewSet)
router.register(r'choices', views.ChoiceViewSet)
router.register(r'vote', views.VoteViewSet)

urlpatterns = [
    url(r'^$', views.login_user, name='login_user'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^', include(router.urls, namespace = 'polls')),
    url(r'^', include(router.urls, namespace = 'choices')),
    url(r'^', include(router.urls, namespace = 'vote')),

]
