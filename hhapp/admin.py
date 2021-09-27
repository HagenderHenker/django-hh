from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Koerperschaften)
admin.site.register(models.Gemeinde)
admin.site.register(models.Haushalt)
admin.site.register(models.Eigenkapital)
admin.site.register(models.Ergebnisentwicklung)
admin.site.register(models.Finanzentwicklung)
admin.site.register(models.InvestKreditentwicklung)
admin.site.register(models.LiqKreditentwicklung)
admin.site.register(models.Investitionsentwicklung)
