from string import ascii_lowercase

from django import forms
from django.contrib import admin
from .models import Class, Station, Assessment


def get_choices() -> list:
    return [(x, x,) for x in (*ascii_lowercase,)]


class ClassForm(forms.ModelForm):

    parallel_class_lower_bound = forms.ChoiceField(choices=get_choices(), label='Parallelklasse',)
    parallel_class_upper_bound = forms.ChoiceField(choices=get_choices(), label='Bis Paralleklasse')
    
    class Meta:
        model = Class
        exclude = ['parallel_class']

    def save(self, commit=True):
        return super(ClassForm, self).save(commit=commit)


class ClassAdmin(admin.ModelAdmin):
    form = ClassForm
    fieldsets = [
        ['', {
            'fields': ['class_level', 'parallel_class_lower_bound']
        }],
        ['Mehrere Parallelklassen auf einmal hinzufügen', {
            'classes': ['collapse'],
            'fields': ['parallel_class_upper_bound'],
        }],
    ]

    def save_model(self, request, obj, form, change):
        lower = form.cleaned_data.get('parallel_class_lower_bound', None)
        upper = form.cleaned_data.get('parallel_class_upper_bound', None)

        if not ord(lower) < ord(upper):
            # User has only set the lower bound and seems to only
            # want to create one records, not many classes at the
            # same time.
            upper = lower

        classes = [
            Class(class_level=obj.class_level,
                  parallel_class=chr(parallel_class)
            ) for parallel_class in range(ord(lower), ord(upper) + 1)
        ]
        Class.objects.bulk_create(classes)

        
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'station_name', 'score']


admin.site.register(Class, ClassAdmin)
admin.site.register(Station)
admin.site.register(Assessment, AssessmentAdmin)
