from django.urls import path
from rest_framework import views
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', views.Userlist.as_view()),
    path('user/detail/<str:pk>/', views.UserDescription.as_view()),
    path('flashcards/', views.Flashcardslist.as_view()),
    path('flashcard/detail/<str:pk>/', views.FlashcardDescription.as_view()),
    path('api-token-auth/', obtain_auth_token)

]