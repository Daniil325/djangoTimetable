from django.contrib import admin
from .models import *


class DepartmentInline(admin.TabularInline):
    model = Department
    prepopulated_fields = {"slug": ("name",)}


class TeacherInline(admin.TabularInline):
    model = Teacher
    prepopulated_fields = {"slug": ("name",)}


class GroupInline(admin.TabularInline):
    model = Group
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    exclude = ['slug']
    inlines = [
        DepartmentInline,
        GroupInline
    ]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        TeacherInline
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'department')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(TypeClass)
class TypeClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(TimeClass)
class TimeClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'group', 'audience', 'type_class', 'time_class', 'subject', 'date', 'num_week')
    exclude = ['num_week']  # убираем поле добавления в админке
