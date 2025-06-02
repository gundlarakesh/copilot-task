from django.urls import path
from .views import ChatbotViewSet

urlpatterns = [
    path('chat-bot/', ChatbotViewSet.as_view({"post":"query_data"}), name='query-data'),
]