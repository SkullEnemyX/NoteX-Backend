from django.urls import path , include
from .views import index,registerUser,changePassword,deleteUser,SignIn,viewNotes,makeNotes,fetchInfo
from rest_framework import routers
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register("authentication",registerUser)

urlpatterns = [
    path('index/',index , name = "index"),
    url(r'^registerUser/', registerUser.as_view()),
    url(r'^deleteUser/', deleteUser.as_view()),
    url(r'^signIn/', SignIn.as_view()),
    url(r'^changePassword/', changePassword.as_view()),
    url(r'^viewNotes/', viewNotes.as_view()),
    url(r'^makeNotes/', makeNotes.as_view()),
    url(r'^fetchInfo/', fetchInfo.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)