

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('category', models.CharField(choices=[('special', '특별한 날'), ('lover', '연인과'), ('company', '회식'), ('family', '가족과'), ('alone', '혼자'), ('activity', '액티비티'), ('friend', '친구와'), ('healing', '힐링')], default='friend', max_length=50)),
                ('location', models.CharField(choices=[('MP', '마포구'), ('GS', '강서구'), ('YC', '양천구'), ('GR', '구로구'), ('YDP', '양천구'), ('GC', '금천구'), ('DJ', '동작구'), ('GA', '관악구'), ('SC', '서초구'), ('GN', '강남구'), ('SP', '송파구'), ('GD', '강동구'), ('SDM', '서대문구'), ('GN', '종로구'), ('EP', '은평구'), ('J', '중구'), ('YS', '용산구'), ('SB', '성북구'), ('GB', '강북구'), ('DB', '도봉구'), ('NW', '노원구'), ('DDM', '동대문구'), ('SD', '성동구'), ('JN', '중랑구'), ('GJ', '광진구')], default='MP', max_length=50)),

                ('created', models.DateTimeField(auto_now=True)),
                ('like_count', models.IntegerField(default=0)),
                ('title1', models.TextField()),
                ('description1', models.TextField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title2', models.TextField()),
                ('description2', models.TextField()),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title3', models.TextField()),
                ('description3', models.TextField()),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('like_users', models.ManyToManyField(null=True, related_name='check_notices', to=settings.AUTH_USER_MODEL)),

                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
