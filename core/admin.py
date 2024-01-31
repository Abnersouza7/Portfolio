from django.contrib import admin

# Register your models here.
from .views import *

admin.site.register(About)
admin.site.register(trajetoria_pessoal)
admin.site.register(trajetoria_profissional)
admin.site.register(Certificate)
