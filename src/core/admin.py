from django.contrib import admin

# Register your models here.

from .models import Feira, SubPrefeitura, Distrito

admin.site.register(Distrito)
admin.site.register(SubPrefeitura)
admin.site.register(Feira)
