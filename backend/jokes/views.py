from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from backend.cars import serializers

from .models import Joke
from .serializers import JokeSerializer
# Create your views here.

# <<<<<<<<<<<<<<< GETS ALL JOKES >>>>>>>>>>>>>>>>>
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_jokes(request):
    jokes = Joke.object.all() # retrieves joke object
    serializer = JokeSerializer(jokes, many=True) # serializes each joke object
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([AllowAny])
def user_jokes(request): 
    if request.method == 'POST':
           serializer = JokeSerializer(data=request.data)
           if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        jokes = Joke.objects.filter(user_id=request.user.id)
        serializer = JokeSerializer(jokes, many=True)
        return Response(serializer.data)    
