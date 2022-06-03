from django.urls import path
from handler import views


urlpatterns = [
    path('api/v1/message', views.get_message),
    path('api/v1/message_confirmation', views.update_message_status),
]
