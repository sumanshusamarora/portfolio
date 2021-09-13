"""
Models
"""
import uuid

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel
from simple_history.models import HistoricalRecords

from .utils import get_upload_path, SKILL_CATEGORY_CHOICES

# Create your models here.
class Professional(TimeStampedModel):
    """

    """
    guid = models.UUIDField(primary_key=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    history = HistoricalRecords()


class Resume(TimeStampedModel):
    """

    """
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    resume = models.FileField(upload_to=get_upload_path)
    history = HistoricalRecords()

class Skill(TimeStampedModel):
    """
    Skills
    """
    category = models.CharField(max_length=255, null=False, blank=False, choices=SKILL_CATEGORY_CHOICES)
    name = models.CharField(max_length=255, null=False, blank=False)
    competency = models.PositiveIntegerField(default=50, validators=[MaxValueValidator(100), MinValueValidator(1)])
    history = HistoricalRecords()
