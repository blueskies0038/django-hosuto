from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = ((GENDER_MALE, "Male"),(GENDER_FEMALE, "Female"),(GENDER_OTHER, "Other"),)

    LANGUAGE_EN = "english"
    LANGUAGE_SP = "spanish"
    LANGUAGE_CN = "chinese"
    LANGUAGE_KR = "korean"

    LANGUAGE_CHOICES = ((LANGUAGE_EN, "Englsih"),(LANGUAGE_SP, "Spanish"),(LANGUAGE_CN, "Chinese"),(LANGUAGE_KR, "Korean"),)

    CURRENCY_USD = "usd"
    CURRENCY_EUR = "eur"
    CURRENCY_CNY = "cny"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"),(CURRENCY_EUR, "EUR"),(CURRENCY_CNY, "CNY"),(CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(upload_to="avatars",  blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10, blank=True)
    superhost = models.BooleanField(default=False)
