from pretalx_iff_dif.models import Dif, YearsReceivedDifSupport, TravelSupportTypes
from pretalx.common.mixins.forms import PublicContent, RequestRequire
from pretalx.cfp.forms.cfp import CfPFormMixin
from i18nfield.forms import I18nModelForm
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django import forms
import pdb


class DifForm(CfPFormMixin, forms.ModelForm):
    travel_support_required = forms.BooleanField(
        label=_('Do you require travel support for IFF 2020?'),
        help_text=_('Because of the huge demand for support, we ask that you don’t request more than what you need to attend. If you have other options to support your participation, we encourage you to explore them early on in order to secure your attendance.'),
        required=False,
    )

    years_received_dif_support = forms.MultipleChoiceField(
        required=False,
        label=_("Which years has the speaker received DiF support?"),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'dif-question'}),
        choices=YearsReceivedDifSupport.get_choices()
    )

    travel_support_types = forms.MultipleChoiceField(
        required=False,
        label=_("Please choose the type of travel support you need"),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'dif-question'}),
        choices=TravelSupportTypes.get_choices()
    )

    speaker_email = forms.EmailField(
        required=False,
        help_text=_("Only one speaker per session can be awarded a travel stipend. For sessions with more than one speaker, please choose the recipient of the stipend"),
        label="Travel stipend awardee email",
    )

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event', None)
        self.user = kwargs.pop('user', None)
        self.readonly = kwargs.pop('readonly', False)

        super().__init__(*args, **kwargs)

        if self.readonly:
            for f in self.fields.values():
                f.disabled = True

    def clean(self):
        data = self.cleaned_data
        if not data.get('travel_support_required', None):
            return {}

        if data.get('years_received_dif_support', None) and data.get('travel_support_types', None):
            return data
        else:
            error = ValidationError(_('Please respond all questions'))
            self.add_error('travel_support_required', error)

    def save(self, *args, **kwargs):
        self.instance.event = self.event
        self.instance.submission = self.submission
        super().save(*args, **kwargs)

    class Meta:
        model = Dif
        fields = [
            'travel_support_required',
            'years_received_dif_support',
            'travel_support_types',
            'speaker_email',
        ]
