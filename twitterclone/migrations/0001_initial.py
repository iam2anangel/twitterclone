# Generated by Django 2.2.1 on 2019-05-20 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('display_name', models.CharField(max_length=50)),
                ('following', models.ManyToManyField(blank=True, to='twitterclone.TwitterUser')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.CharField(max_length=140)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterclone.TwitterUser')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was_viewed', models.BooleanField(default=False)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterclone.Tweet')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterclone.TwitterUser')),
            ],
        ),
    ]
