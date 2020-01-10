from django.contrib import admin
from PCBuilder import models as m

admin.site.register(m.Category)
admin.site.register(m.Price)
admin.site.register(m.Part)
admin.site.register(m.FinalProduct)
