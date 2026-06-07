from django.contrib import admin
from .models import Skill, Experience, ExperienceBullet, Project, ProjectTag, Stat


class ExperienceBulletInline(admin.TabularInline):
    model = ExperienceBullet
    extra = 1


class ProjectTagInline(admin.TabularInline):
    model = ProjectTag
    extra = 1


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_filter = ['category']
    ordering = ['category', 'order']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'start_date', 'end_date', 'is_current']
    inlines = [ExperienceBulletInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    inlines = [ProjectTagInline]


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ['value', 'label', 'order']
