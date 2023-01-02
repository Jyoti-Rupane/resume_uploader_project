from django.shortcuts import render
from rest_framework.response import Response
from .models import profile
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class ProfileView(APIView):
    def post(self,request,format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'resume uploaded successfully','status':'success','candidate':serializer.data})
        return Response(serializer.errors)

    def get(self,request,format=None):
        candidate=profile.objects.all()
        serializer=ProfileSerializer(candidate,many=True)
        return Response({'status':'success','candidate':'serializer.data'},status=status.HTTP_200_OK)



