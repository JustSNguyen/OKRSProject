from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

from .project import Project
from .user import User


class ProjectMembership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(null=True, blank=True)
    role = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)])
