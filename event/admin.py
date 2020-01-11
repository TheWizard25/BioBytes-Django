from django.contrib import admin

from .models import Event



from django import forms

class EventForm(forms.ModelForm ):
    event_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

class Meta:
    model = Event
    
class EventAdmin(admin.ModelAdmin):
    form = EventForm
    
admin.site.register(Event, EventAdmin)