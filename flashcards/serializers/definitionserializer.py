from rest_framework import serializers
from flashcards.models.definitions import Word


class WordSerializer(serializers.HyperlinkedModelSerializer):
    words = serializers.HyperlinkedRelatedField(many=True, view_name='word-detail', read_only=True)

    class Meta:
        model = Word
        fields = ('url', 'words')
