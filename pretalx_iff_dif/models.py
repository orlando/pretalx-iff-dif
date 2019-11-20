from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

from pretalx.common.choices import Choices


class YearsReceivedDifSupport(Choices):
    NEVER = 'never'
    Y2017 = '2017'
    Y2018 = '2018'
    Y2019 = '2019'

    valid_choices = [
        (NEVER, _('Have never received DIF support')),
        (Y2017, _('2017')),
        (Y2018, _('2018')),
        (Y2019, _('2019')),
    ]


class TravelSupportTypes(Choices):
    HOTEL = 'hotel'
    FLIGHT = 'flight'
    DAILY_PER_DIEM = 'daily_per_diem'

    valid_choices = [
        (HOTEL, _('Hotel')),
        (FLIGHT, _('Flight')),
        (DAILY_PER_DIEM, _('Daily Per Diem')),
    ]


class DifStates(Choices):
    SUBMITTED = 'submitted'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    valid_choices = [
        (SUBMITTED, _('submitted')),
        (ACCEPTED, _('accepted')),
        (REJECTED, _('rejected')),
    ]

    valid_next_states = {
        SUBMITTED: (REJECTED, ACCEPTED),
        REJECTED: (ACCEPTED, SUBMITTED),
        ACCEPTED: (REJECTED, SUBMITTED),
    }


class Dif(models.Model):
    event = models.ForeignKey(
        to='event.Event',
        on_delete=models.CASCADE,
        related_name='difs'
    )
    user = models.ForeignKey(
        to='person.User',
        on_delete=models.CASCADE,
        related_name='difs',
    )
    submission = models.ForeignKey(
        to='submission.Submission',
        on_delete=models.CASCADE,
        related_name='dif',
    )
    years_received_dif_support = ArrayField(
        models.CharField(
            choices=YearsReceivedDifSupport.get_choices(),
            max_length=YearsReceivedDifSupport.get_max_length(),
            default=YearsReceivedDifSupport.NEVER
        ),
    )
    travel_support_types = ArrayField(
        models.CharField(
            choices=TravelSupportTypes.get_choices(),
            max_length=TravelSupportTypes.get_max_length(),
            default=TravelSupportTypes.HOTEL
        ),
    )
    speaker_email = models.EmailField(
        max_length=255,
    )
    state = models.CharField(
        max_length=DifStates.get_max_length(),
        choices=DifStates.get_choices(),
        default=DifStates.SUBMITTED,
        verbose_name=_('Submission state'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def readable_travel_support_types(self):
        array = []
        for support_type in self.travel_support_types:
            array.append(support_type.replace('_', ' '))

        return ", ".join(array)

    def readable_years_received_dif_support(self):
        array = []
        for year in self.years_received_dif_support:
            array.append(year)

        return ", ".join(array)

    def readable_speaker_email(self):
        return self.speaker_email or self.user.email
