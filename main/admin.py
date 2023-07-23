from string import ascii_lowercase

from django import forms
from django.contrib import admin, messages
from .models import Class, Station, Assessment


ASCII_LOWERCASE = [
    (x, x,) for x in (*ascii_lowercase,)
]


class ClassForm(forms.ModelForm):
    parallel_class_lower_bound = forms.ChoiceField(choices=ASCII_LOWERCASE, label='Parallelklasse',)
    parallel_class_upper_bound = forms.ChoiceField(choices=ASCII_LOWERCASE, label='Bis Paralleklasse')
    
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

    def response_add(self, request, obj, post_url_continue=None):
        response = super().response_add(request, obj, post_url_continue)

        # Remove default message
        storage = messages.get_messages(request)
        try:
            del storage._queued_messages[-1]
            print('Deleted')
        except KeyError:
            pass

        return response

    def save_model(self, request, obj, form, change):
        lower = form.cleaned_data.get('parallel_class_lower_bound', None)
        upper = form.cleaned_data.get('parallel_class_upper_bound', None)

        if not ord(lower) < ord(upper):
            # User has only set the lower bound and seems to only
            # want to create one record, not many classes at once.
            upper = lower

        classes = [
            Class(class_level=obj.class_level,
                  parallel_class=chr(parallel_class)
            ) for parallel_class in range(ord(lower), ord(upper) + 1)
        ]
        Class.objects.bulk_create(classes)
        
        if len(classes) == 1:
            message = f'Klasse „{str(classes[0])}“ wurde erfolgreich hinzugefügt.'
        else:
            message = f'Klassen „{str(classes[0])}“'
            for class_ in classes[1:-2]:
                message += f', „{str(class_)}“'
            message += f'und „{str(classes[-1])}“ wurden erfolgreich hinzugefügt.'

        messages.add_message(request, messages.INFO, message)

        
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'station_name', 'score']


admin.site.register(Class, ClassAdmin)
admin.site.register(Station)
admin.site.register(Assessment, AssessmentAdmin)
