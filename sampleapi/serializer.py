from rest_framework import serializers
from sampleapi.models import Person, Species, Image

class PersonSerializer(serializers.ModelSerializer):
   class Meta:
       model = Person
       fields = ('id', 'name', 'birth_year', 'eye_color', 'species')

class SpeciesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Species
       fields = ('id', 'name', 'classification', 'language')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'