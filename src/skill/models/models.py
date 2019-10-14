from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractUser
from ..utils import unique_slug_generator


class Post(models.Model):
    objects = None
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp", "-updated"]


# Django will add 's'

class Categorie(models.Model):
    name = models.TextField()
    mnemo = models.TextField()
    description = models.TextField()
    test_id = models.IntegerField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


class Course(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    unlime_price = models.IntegerField()
    time = models.IntegerField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)
