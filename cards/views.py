from re import A
from django.http.response import Http404
from rest_framework.response import Response
from .models import User, Flashcards
from .serializer import FlashcardsSerializer, UserSerializer
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from rest_framework import status



# Create your views here.
class Userlist(APIView):
    def get(self,request,format=None):
        all_users = User.objects.all()
        serializers = UserSerializer(all_users, many=True)
        return Response(serializers.data)

    permission_classes = (IsAdminOrReadOnly,)
    def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404

    def get(self,request,pk,format=None):
        user=self.get_user(pk)
        serializer=UserSerializer(user)
        return Response(serializer.data)



class Flashcardslist(APIView):
    def get(self,request,format=None):
        flashcards = Flashcards.objects.all()
        serializer = FlashcardsSerializer(flashcards, many=True)
        return Response(serializer.data)

    permission_classes = (IsAdminOrReadOnly,)
    def post(self,request,format=None):
        serializer = FlashcardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FlashcardDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_flashcard(self, pk):
        try:
            return Flashcards.objects.get(id=pk)
        except Flashcards.DoesNotExist:
            return 'Not found'

    def get(self,request,pk,format=None):
        flashcard=self.get_flashcard(pk)
        serializer=FlashcardsSerializer(flashcard)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        flashcard = self.get_flashcard(pk)
        serializer=FlashcardsSerializer(flashcard, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        flashcard=self.get_flashcard(pk)
        flashcard.delete()
        return Response('Flashcard deleted')











