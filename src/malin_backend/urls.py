from django.contrib import admin
from django.urls import path, include
from core import views
from core.views import CustomerView, SiteImagesView, ArticlesView, SiteImageView, ArticleView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('malingreats/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('customer', CustomerView.as_view(), name='customer'),
    path('images', SiteImagesView.as_view(), name='images'),
    path('images/<int:pk>', SiteImageView.as_view(), name='images'),
    path('articles', ArticlesView.as_view(), name='articles'),
    path('articles/<int:pk>', ArticleView.as_view(), name='articles'),

    path('agric-signup', views.AgricSignUpEmail, name='agric-signup'),
    path('retail-signup', views.RetailSignUpEmail, name='retail-signup'),
    path('edu-signup', views.EduSignUpEmail, name='edu-signup'),

    path('contact-email', views.ContactEmail, name='contact-email'),
    path('enquiry-email', views.EnquiryEmail, name='enquiry-email'),
    path('newsletter', views.Newsletter, name='newsletter'),
    path('quotation', views.Quotation, name='quotation'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
