from rest_framework import serializers
from .models import Joke

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<


class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = ['id', 'setup', 'punchline']
        depth = 1
