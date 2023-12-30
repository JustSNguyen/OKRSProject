from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

from .project import Project


class ProjectTag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)])
