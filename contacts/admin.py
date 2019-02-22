from django.contrib import admin
from .models import Feedback, FeedbackCategory


@admin.register(Feedback)
class FeedbackModelAdmin(admin.ModelAdmin):

    list_display = (
        'category',
        'name',
        'email',
        'content'
    )


admin.site.register(FeedbackCategory)
