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
   ('MP', 'mapo'),
   ('GS', 'gangseo'),
   ('YC', 'yangcheon'),
   ('GR', 'guro'),
   ('YDP', 'yeongdeungpo'),
   ('GC', 'geumcheon'),
   ('DJ', 'dongjak'),
   ('GA', 'gwanak'),
   ('SC', 'seocho'),
   ('GN', 'gangnam'),
   ('SP', 'songpa'),
   ('GD', 'gangdong'),
   ('SDM', 'seodaemun'),
   ('GN', 'jongno'),
   ('EP','eunpyeong'),
   ('J','jung'),
   ('YS', 'yongsan'),
   ('SB', 'seongbuk'),
   ('GB', 'gangbuk'),
   ('DB', 'dobong'),
   ('NW', 'nowon'),
   ('DDM', 'dongdaemun'),
   ('SD', 'seongdong'),
   ('JN', 'jungnang'),
   ('GJ', 'gwangjin')
)
    # Post 제목
    title = models.TextField()
    category = models.CharField(max_length = 50, choices = CATEGORY_CHOICES,default='friend')
    location = models.CharField(max_length = 50, choices = LOCATION_choice)

    user = models.ForeignKey(User,on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(User,related_name='check_notices',blank=True)
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
