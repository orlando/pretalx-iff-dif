from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (
    ListView
)

from pretalx_iff_dif.models import Dif
from pretalx.common.mixins.views import PermissionRequired


class PermMixin(PermissionRequired):
    permission_required = 'orga.change_settings'

    def get_permission_object(self):
        return self.request.event


def perm(func):
    return func


perm_annotation = perm


class DifList(PermMixin, ListView):
    model = Dif
    context_object_name = 'difs'
    template_name = 'pretalx_iff_dif/dif_list.html'

    def get_queryset(self):
        return self.request.event.difs.all().order_by('created_at')
