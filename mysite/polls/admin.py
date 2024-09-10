from django.contrib import admin

# Register your models here.
from .models import Question,Person

admin.site.register(Question)
admin.site.register(Person)