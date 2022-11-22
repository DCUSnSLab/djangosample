from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from sampleapi.serializer import PersonSerializer, SpeciesSerializer, ImageSerializer
from sampleapi.models import Person, Species, Image

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


class ImageViewAPI(APIView):
   parser_classes = (MultiPartParser, FormParser)

   def get(self, request, *args, **kwargs):
      posts = Image.objects.all()
      serializer = ImageSerializer(posts, many=True)
      return Response(serializer.data)