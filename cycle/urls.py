from rest_framework.routers import DefaultRouter
from cycle.views import CyclePricing

router = DefaultRouter(trailing_slash=False)
router.register("", CyclePricing, basename='cycle')

urlpatterns = router.urls
