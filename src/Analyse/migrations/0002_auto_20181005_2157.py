# Generated by Django 2.1.1 on 2018-10-05 16:27

import Analyse.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Analyse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decision', models.TextField()),
                ('decisionfor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Analyse.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingname', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 5, 21, 57, 44, 370438))),
                ('recording', models.FileField(upload_to=Analyse.models.upload_audio_path)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingAttendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendee', to=settings.AUTH_USER_MODEL)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conductor', to=settings.AUTH_USER_MODEL)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Analyse.Meeting')),
            ],
        ),
        migrations.AddField(
            model_name='decision',
            name='meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Analyse.Meeting'),
        ),
    ]
