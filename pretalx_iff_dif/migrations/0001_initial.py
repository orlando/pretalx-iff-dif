# Generated by Django 2.2.7 on 2019-11-20 03:10

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0021_auto_20190429_0750'),
        ('submission', '0042_question_is_visible_to_reviewers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('years_received_dif_support', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='never', max_length=5), size=None)),
                ('travel_support_types', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='hotel', max_length=14), size=None)),
                ('speaker_email', models.EmailField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='difs', to='event.Event')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dif', to='submission.Submission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='difs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
