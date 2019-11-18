from django.conf.urls import url
from pretalx.event.models.event import SLUG_CHARS

from .views import DifList

urlpatterns = [
    url(
        fr'^orga/event/(?P<event>[{SLUG_CHARS}]+)/dif/$',
        DifList.as_view(),
        name='dif.list',
    )
]
