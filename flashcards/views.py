from rest_framework import viewsets
from flashcards.models.definitions import Word
from flashcards.serializers.definitionserializer import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
