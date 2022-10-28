from django.contrib import admin

from women.apps import WomenConfig
from women.models import Women, Category

# Register your models here.
admin.site.register(Women)
admin.site.register(Category)
