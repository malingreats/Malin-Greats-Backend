from django.contrib import admin

from .models import Articles, SiteImages, Items


admin.site.site_header = "MALIN GREATS ADMIN"


admin.site.register(Articles)
admin.site.register(SiteImages)
admin.site.register(Items)