from django.db import models
from users.models import User


class Post(models.Model):
    user = models.ForeignKey(User, verbose_name="가계부 작성자", on_delete=models.CASCADE, related_name="post_user")
    account = models.IntegerField(verbose_name="가계부 금액")
    content = models.CharField(verbose_name="가계부 메모", max_length=50)
    created_at = models.DateTimeField(verbose_name="가계부 작성 시간", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="가계부 수정 시간", auto_now=True)

    def __str__(self):
        return str(f"{self.account} / {self.content}")
