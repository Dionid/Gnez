from django.conf.urls import url
from .views import UsersList, VkView

urlpatterns = [
    url(r'^vk/$', VkView.as_view()),
    url(r'^users/$', UsersList.as_view()),
]
