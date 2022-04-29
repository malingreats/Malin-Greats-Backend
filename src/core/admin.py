from django.contrib import admin

from .models import Articles, Newsletter, SiteImages, Items, AgricultureSignUp, RetailSignUp, EducationSignUp, ContactEmail, EnquiryEmail, Newsletter

admin.site.site_header = "MALIN GREATS ADMIN"


admin.site.register(Articles)
admin.site.register(SiteImages)
admin.site.register(Items)
admin.site.register(AgricultureSignUp)
admin.site.register(RetailSignUp)
admin.site.register(EducationSignUp)
admin.site.register(ContactEmail)
admin.site.register(EnquiryEmail)
admin.site.register(Newsletter)
