import os

from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.db import models


def _rename_file(username, filename):
    time = timezone.now()
    new_name = '_'.join([username, time.date(), time.time(), filename])
    return new_name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class File(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, null=True, blank=True)
    file = models.FileField(
        null=True,
        blank=True,
        upload_to=f'files/'
    )
    descriptions = models.TextField()
    upload_data = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name or self.file.name


    def extension(self):
        absolute_path, extension = os.path.splitext(self.file.name)
        return extension


    def get_absolute_url(self):
        return reverse('file-detail', kwargs={'pk': self.pk})

