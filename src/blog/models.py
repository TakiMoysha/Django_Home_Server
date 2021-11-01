import os

from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.db import models

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
        upload_to=
            (lambda instance, filename: f'files/{instance.author.username}/{filename}'),
    )
    descriptions = models.TextField(null=True, blank=True)
    upload_data = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name or self.file.name


    def save(self, *args, **kwargs):
        if (self.name == None):
            self.name = self.file.name
        super(File, self).save(*args, **kwargs)


    def extension(self):
        absolute_path, var_extension = os.path.splitext(self.file.name)
        return var_extension


    def get_absolute_url(self):
        return reverse('file-detail', kwargs={'pk': self.pk})

