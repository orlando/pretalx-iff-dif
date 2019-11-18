from django.dispatch import receiver
from django.urls import resolve, reverse
from django.utils.translation import ugettext_lazy as _

from pretalx.orga.signals import nav_event


@receiver(nav_event, dispatch_uid='dif_nav_entry')
def navbar_info(sender, request, **kwargs):
    url = resolve(request.path_info)
    kwargs = {'event': request.event.slug}
    return [
        {
            'label': _('DiF requests'),
            'icon': 'users',
            'url': reverse('plugins:pretalx_iff_dif:dif.list', kwargs=kwargs),
            'active': 'dif' in url.url_name,
        }
    ]
