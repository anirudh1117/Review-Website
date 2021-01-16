from django.contrib import admin
from .models import AddCourse


class AddCourseAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'course_name', 'instructor_name', 'category','description', 'is_published')
    list_display_links = ('user_id', 'course_name')
    search_fields = ('course_name', 'category',)
    list_editable = ('is_published',)
    list_per_page = 25


admin.site.register(AddCourse,AddCourseAdmin)