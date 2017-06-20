from django.conf.urls import url
from forms.views import OwnerFormList, SeekerFormList

urlpatterns = [
    url(r'^seeker', SeekerFormList.as_view()),
    url(r'^owner', OwnerFormList.as_view()),
]
