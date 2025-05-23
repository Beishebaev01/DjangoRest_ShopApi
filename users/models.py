from django.db import models
from django.contrib.auth.models import User
import random

def generate_code():
    return '{:06d}'.format(random.randint(0, 999999))

class VerificationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='verification_code')
    code = models.CharField(max_length=6, default=generate_code)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'Код для {self.user.username}: {self.code}'
