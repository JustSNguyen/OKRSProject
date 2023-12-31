# Generated by Django 4.2.6 on 2023-12-30 12:43

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_user_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.TextField(blank=True, default='Untitled', max_length=100, validators=[django.core.validators.MinLengthValidator(10)])),
                ('description', models.TextField(max_length=300, validators=[django.core.validators.MinLengthValidator(300)])),
                ('last_edited', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.PositiveIntegerField(default=1703940182),
        ),
    ]
