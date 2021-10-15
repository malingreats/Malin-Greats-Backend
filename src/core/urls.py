from django.urls import include, path

from rest_framework import routers

from core.views import ItemsViewSet, DetailsViewSet, SiteImagesView



router = routers.DefaultRouter()
router.register(r'items', ItemsViewSet)
router.register(r'details', DetailsViewSet)


urlpatterns = [
	path('', include(router.urls)),
	
]