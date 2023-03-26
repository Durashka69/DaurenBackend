from rest_framework import serializers

from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'is_businessman',
            'title',
            'description',
            'phone_number',
            'image',
            'date_created'
        )
        read_only_fields = ('user',)
