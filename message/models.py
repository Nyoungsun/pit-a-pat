from django.db import models
from papers.models import Rolling_paper
from django.contrib.auth.models import User as Auth_User
from django.utils import timezone

# Create your models here.

# 메세지 테이블
class Message(models.Model) :
    message_number = models.AutoField(primary_key=True)
    paper_number = models.ForeignKey(Rolling_paper, on_delete=models.CASCADE, to_field="paper_number", db_column="paper_number")
    nickname = models.ForeignKey(Auth_User, on_delete=models.CASCADE, to_field="username", db_column="nickname")
    content = models.CharField(max_length=500, blank=True)
    wrote = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    class Meta :
        db_table = "Message"
