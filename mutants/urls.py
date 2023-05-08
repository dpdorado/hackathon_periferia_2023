from rest_framework.routers import SimpleRouter
from .api import PersonViewSet, StatsViewSet
from django.urls import path

router = SimpleRouter()

router.urls.extend([
    #path('api/mutant/', PersonViewSet.as_view({'post': 'create', 'get': 'list'}), name='mutant'),
    path('api/mutant/', PersonViewSet.as_view({'post': 'create', 'get': 'list'}), name='mutant'),
])
router.urls.extend([
    path('api/stats/', StatsViewSet.as_view({'get': 'list'}), name='stats'),
])

urlpatterns = router.urls