from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'receipeapp'

urlpatterns = [

    path('', views.add_receipe, name='add_receipe'),
    path('view_receipe/', views.view_receipe, name='view_receipe'),
    path('view_receipe/delete_receipe/<id>/', views.delete_receipe, name='delete_receipe'),
    path('view_receipe/update_receipe/<id>/', views.update_receipe,name='update_receipe'),

    path('login_page/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('logout_page/', views.logout_page, name='logout_page')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)