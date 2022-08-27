from sre_parse import CATEGORIES
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    CATEGORY_CHOICES = (
        ('special', '특별한 날'),
        ('lover', '연인과'),
        ('company', '회식'),
        ('family', '가족과'),
        ('alone', '혼자'),
        ('activity', '액티비티'),
        ('friend', '친구와'),
        ('healing','힐링'),
    )



    LOCATION_choice = (
   ('MP', '마포구'),
   ('GS', '강서구'),
   ('YC', '양천구'),
   ('GR', '구로구'),
   ('YDP', '영등포구'),
   ('GC', '금천구'),
   ('DJ', '동작구'),
   ('GA', '관악구'),
   ('SC', '서초구'),
   ('GN', '강남구'),
   ('SP', '송파구'),
   ('GD', '강동구'),
   ('SDM', '서대문구'),
   ('GN', '종로구'),
   ('EP','은평구'),
   ('J','중구'),
   ('YS', '용산구'),
   ('SB', '성북구'),
   ('GB', '강북구'),
   ('DB', '도봉구'),
   ('NW', '노원구'),
   ('DDM', '동대문구'),
   ('SD', '성동구'),
   ('JN', '중랑구'),
   ('GJ', '광진구')
)
    # Post 제목
    title = models.TextField()
    category = models.CharField(max_length = 50, choices = CATEGORY_CHOICES,default='friend')
    location = models.CharField(max_length = 50, choices = LOCATION_choice, default='MP')

    user = models.ForeignKey(User,on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(User,related_name='check_notices')
    like_count = models.IntegerField(default=0)


    title1 = models.TextField()        # 장소 이름 1
    description1 = models.TextField()
    image1 = models.ImageField(upload_to='images/',blank=True, null=True)

    title2 = models.TextField()
    description2 = models.TextField()
    image2 = models.ImageField(upload_to='images/',blank=True, null=True)

    title3 = models.TextField()
    description3 = models.TextField()
    image3 = models.ImageField(upload_to='images/',blank=True, null=True)


    def __str__(self):
        return "{} - {}".format(self.title, self.category)

class HashTag(models.Model):
    hashtag = models.CharField(max_length=100)
    
    def __str__(self):
        return self.hashtag

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text


