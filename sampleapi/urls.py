from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from sampleapi.views import PersonViewAPI, PersonListViewAPI, SpeciesViewSet, ImageViewAPI

router = routers.DefaultRouter()
#router.register(r'people', PersonViewAPI)
router.register(r'species', SpeciesViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('peoples/', PersonListViewAPI.as_view(), name='peoples'),
   path('people/<int:id>', PersonViewAPI.as_view(), name='people'),
   path('images/', ImageViewAPI.as_view(), name='image_list'),
   # path('people/<int:id>', PersonViewAPI.as_view(), name='people')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)