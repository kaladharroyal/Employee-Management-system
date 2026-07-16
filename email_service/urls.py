from rest_framework.routers import DefaultRouter
from .views import EmailLogViewSet, EmailTemplateViewSet, SenderEmailViewSet

router = DefaultRouter()
router.register(r'emails', EmailLogViewSet, basename='emails')
router.register(r'templates', EmailTemplateViewSet, basename='templates')
router.register(r'senders', SenderEmailViewSet, basename='senders')

urlpatterns = router.urls