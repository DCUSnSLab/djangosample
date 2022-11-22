from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from sampleapi.serializer import PersonSerializer, SpeciesSerializer
from sampleapi.models import Person, Species

class PersonListViewAPI(APIView):
   def get(self, request): # GET for peoples
      queryset = Person.objects.all()
      serializer = PersonSerializer(queryset, many=True)
      return Response(serializer.data)

   def post(self, request):
      pass

class PersonViewAPI(APIView):
   def get(self, request, id): # GET for peoples
      queryset = Person.objects.filter(id=id)
      serializer = PersonSerializer(queryset, many=True)
      return Response(serializer.data)

   def post(self, request):
      pass

class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Species.objects.all()
   serializer_class = SpeciesSerializer