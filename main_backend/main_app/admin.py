from django.contrib import admin
from .models import User, UserAdmin, Project, ProjectTag, ProjectMembership

admin.site.register(User, UserAdmin)
admin.site.register(Project)
admin.site.register(ProjectTag)
admin.site.register(ProjectMembership)
