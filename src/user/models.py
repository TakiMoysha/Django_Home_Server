import os
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
        null=True,
    )

    image = models.ImageField(
        default='images/profile_pics/default_avatar.jpg',
        upload_to=
            (lambda instance, filename: f'images/profile_pics/{instance.user.username}/{filename}'),
    )

    class Meta:
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'Profile {self.user.username}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 512 or img.width > 512:
            output_size = (512, 512)
            img.thumbnail(output_size)
            img.save(self.image.path)

