from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home,name='home'),
    path('', views.user_login,name='user_login'),
    path('log_out', views.log_out,name='log_out'),
    path('sinup_user', views.sinup_user,name='sinup_user'),
    path('input_item', views.input_item,name='input_item'),
    path('input_sales', views.input_sales,name='input_sales'),
    path('update_item/<str:NP>', views.update_item,name='update_item'),
    path('update_sales/<str:NP>', views.update_sales,name='update_sales'),
    path('delete_item/<str:NP>', views.delete_item,name='delete_item'),
    path('delete_sales/<str:NP>', views.delete_sales,name='delete_sales'),
]
