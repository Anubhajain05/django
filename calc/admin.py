from tinymce.widgets import TinyMCE
from django.db import models

from django.contrib import admin

from .models import Tutorial, add_product, TutorialSeries, TutorialCategory



class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]}),
        ("Series", {'fields': ["tutorial_series"]}),


    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(add_product)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)



# Register your models here.
