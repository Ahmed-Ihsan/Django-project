from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path("", views.for_user ,name="index"),
	path("img/", views.for_img ,name="img"),
	path("in_po/", views.input_post ,name="in_po"),
	path("in_us/", views.input_user ,name="in_us"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
