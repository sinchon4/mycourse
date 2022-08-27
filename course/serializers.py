from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user','created','like_users','like_count','title1','category1',
        'location1','image1','title2','category2','location2','image2','title3','category3','location3','image3']