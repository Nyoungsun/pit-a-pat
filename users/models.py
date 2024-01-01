from django.db import models
from django.utils import timezone

# Create your models here.

# 유저 테이블
class User(models.Model) :
    id = models.CharField(max_length=30, primary_key=True)
    pwd = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    papers = models.IntegerField(default=0)
    messages = models.IntegerField(default=0)
    joined = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    class Meta :
        db_table = "User"
