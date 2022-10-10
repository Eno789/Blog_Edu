from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

class User(AbstractUser):
    class Gender(models.TextChoices):
        Male = "M", "남성"
        Female = "F", "여성"
        X = "X", "X"

    gender = models.CharField(max_length=10, default='X', choices=Gender.choices)
    phone_number = models.CharField(max_length=13, blank=True,
                                    validators=[RegexValidator(r"010-?[1-9]\d{3}-?\d{4}$")])
    email_url = models.EmailField(max_length=29, blank=True,
                                  validators=[RegexValidator(r"^[0-9]{9}@[office.hanseo]+\.[ac.kr]+$")])
    @property
    def name(self):
        return f"{self.first_name}{self.last_name}"

