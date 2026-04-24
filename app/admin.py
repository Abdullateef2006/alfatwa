from django.contrib import admin
from .models import *

class QuestionsInline(admin.TabularInline):
    model = Questions
    extra = 1  # Provides 1 empty row to add a new question

class EpisodesAdmin(admin.ModelAdmin):
    inlines = [QuestionsInline]

admin.site.register(Lecture)
admin.site.register(Episodes, EpisodesAdmin)
admin.site.register(Questions)
