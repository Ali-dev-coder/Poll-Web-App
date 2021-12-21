from django.contrib import admin
from .models import pollmodel
# Register your models here.
@admin.register(pollmodel)
class polladmin(admin.ModelAdmin):
    list_display = ['id','poll_question','poll_option_one','poll_option_two','poll_option_three']
