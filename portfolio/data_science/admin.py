from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import *

# Register your models here.
class ProfessionalAdmin(SimpleHistoryAdmin):
    readonly_fields = ("guid",)


admin.site.register(Professional, ProfessionalAdmin)


class SkillAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(Skill, SkillAdmin)


class ResumeAdmin(SimpleHistoryAdmin):
    pass


admin.site.register(Resume, ResumeAdmin)