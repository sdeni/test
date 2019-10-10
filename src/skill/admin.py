from django.contrib import admin
from .models.models import Course
from .models.models import Categorie
from .models.models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post


class CourseModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Course


admin.site.register(Post, PostModelAdmin)
admin.site.register(Course)
admin.site.register(Categorie)