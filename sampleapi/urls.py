from django.urls import include, path
from rest_framework import routers
from sampleapi.views import PersonViewAPI, PersonListViewAPI, SpeciesViewSet

router = routers.DefaultRouter()
#router.register(r'people', PersonViewAPI)
router.register(r'species', SpeciesViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('peoples/', PersonListViewAPI.as_view(), name='peoples'),
   path('people/<int:id>', PersonViewAPI.as_view(), name='people'),
   # path('people/<int:id>', PersonViewAPI.as_view(), name='people')
]