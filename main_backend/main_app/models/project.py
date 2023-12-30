from django.db import models
from django.core.validators import MinLengthValidator
import uuid


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=100,
                            default="Untitled", validators=[MinLengthValidator(10)], blank=True)
    description = models.TextField(
        max_length=300, validators=[MinLengthValidator(300)])
    last_edited = models.DateTimeField(null=True, blank=True)
