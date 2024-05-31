from django.contrib import admin
from .models import CustomUser, Subject, Lesson, Score, UserProfile, Test, Answer
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ('wide',),
                "fields": ("username", "email", "first_name", "last_name","grade", "password1", "password2"),
            },
        ),
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Score)
admin.site.register(Test)
admin.site.register(Answer)
admin.site.register(UserProfile)
