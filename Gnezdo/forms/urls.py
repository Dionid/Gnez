from django.conf.urls import url
from forms.views import OwnerFormList, SeekerFormList, SeekerFormDetail

urlpatterns = [
    url(r'^seeker/$', SeekerFormList.as_view()),
    url(r'^seeker/(?P<pk>[0-9]+)/$', SeekerFormDetail.as_view()),
    url(r'^owner/$', OwnerFormList.as_view()),
]
