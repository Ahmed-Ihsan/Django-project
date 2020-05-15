from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path("", views.for_user ,name="index"),
	path("img/", views.for_img ,name="img"),
	path("in_po/", views.input_post ,name="in_po"),
	path("in_us/", views.input_user ,name="in_us"),
	path("<int:id>", views.id_user ,name="id_us"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)
