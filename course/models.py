from sre_parse import CATEGORIES
from django.db import models

# Create your models here.

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
categoty= models.TextField( choices = CATEGORY_CHOICES,default='friend')
