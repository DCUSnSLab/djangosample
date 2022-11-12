from rest_framework import viewsets
from sampleapi.serializer import PersonSerializer, SpeciesSerializer
from sampleapi.models import Person, Species

class PersonViewSet(viewsets.ModelViewSet):
   queryset = Person.objects.all()
   serializer_class = PersonSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Species.objects.all()
   serializer_class = SpeciesSerializer