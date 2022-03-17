from django.contrib import admin
from .models import Speech, Speechlength

class SpeechAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'price',
        'speechlength'
    )


admin.site.register(Speech)
admin.site.register(Speechlength)
