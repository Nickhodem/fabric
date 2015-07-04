from django.contrib import admin
from knitting.models import *
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','vacancy', 'start_date')
class TutorAdmin(admin.ModelAdmin):
    list_display = ('name','surname')
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'hashname','paid')

admin.site.register(Course, PageAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Student, StudentAdmin)
