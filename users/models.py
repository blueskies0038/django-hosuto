import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string

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

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_GOOGLE = "google"

    LOGIN_CHOICES = ((LOGIN_EMAIL, "Email"), (LOGIN_GITHUB, "Github"), (LOGIN_GOOGLE, "Google"),)

    avatar = models.ImageField(upload_to="avatars",  blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10, blank=True)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)
    login_method = models.CharField(max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            message = render_to_string("emails/verify_email.html", {'secret': secret})
            send_mail("Verify Airbnb Account", message, settings.EMAIL_FROM, [self.email], fail_silently=True,)
            self.save()

