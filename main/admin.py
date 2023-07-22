from django.contrib import admin
from .models import Class, Station, Assessment


class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'station_name', 'score']


admin.site.register(Class)
admin.site.register(Station)
admin.site.register(Assessment, AssessmentAdmin)
