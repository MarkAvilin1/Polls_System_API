from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Polls)
admin.site.register(Questions)
admin.site.register(Choices)
admin.site.register(Answers)
