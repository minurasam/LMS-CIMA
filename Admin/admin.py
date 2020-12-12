from django.contrib import admin
from .models import Level, Course, Module, Lecturer, Student


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['level_No', 'level']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'Cima_ID', 'name', 'email', 'level', 'lecturer', 'membership', 'lecturer']
    list_filter = ['level', 'lecturer', 'name']
    search_fields = ['Cima_ID', 'name']


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'name', 'level', 'lecturer']
    list_filter = ['level', 'lecturer', 'name']
    search_fields = ['course_id', 'name']
    inlines = [ModuleInline]
