from django.shortcuts import render
from .models import Post
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  PostSerializer

class TestView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request,*args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PostView(generics.GenericAPIView)