from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers

from .models.models import Post

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, read_only=True)
    class Meta:
        model = User
        fields = [
            'username',  
            'first_name',
            'last_name',
            ]
    

class PostSerializer(serializers.ModelSerializer):
    url             = serializers.HyperlinkedIdentityField(
                            # view_name='skill-api:detail',
                            view_name='detail',
                            lookup_field='slug'
                            )
    user            = UserPublicSerializer(read_only=True)
    publish         = serializers.DateField(default=timezone.now())
    
    class Meta:
        model = Post
        fields = [
            'url',
            'slug',
            'user',
            'title',
            'content',
            'draft',
            'publish',
            'updated',
            'timestamp',
        ]