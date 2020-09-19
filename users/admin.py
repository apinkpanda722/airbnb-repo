from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class UserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
<<<<<<< HEAD
        (
            "Custom Profile",
            {"fields": ("avatar", "superhost", "favs")},
        ),
=======
        ("Custom Profile", {"fields": ("avatar", "superhost",)},),
>>>>>>> cc2656b759cba23d39d51007debe9d5b6390a042
    )

    list_display = UserAdmin.list_display + ("room_count",)
