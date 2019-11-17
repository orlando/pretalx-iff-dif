from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = "pretalx_iff_dif"
    verbose_name = "Pretalx IFF Diversity and Inclusion Fund plugin"

    class PretalxPluginMeta:
        name = ugettext_lazy("Pretalx IFF Diversity and Inclusion Fund plugin")
        author = "Orlando Del Aguila"
        description = ugettext_lazy("Plugin to add a way to manage speakers applying for the IFF Diversity and Inclusion Fund")
        visible = True
        version = "0.0.0"

    def ready(self):
        from . import signals  # NOQA


default_app_config = "pretalx_iff_dif.PluginApp"
