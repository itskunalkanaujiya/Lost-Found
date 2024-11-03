from django.contrib import admin
from django.urls import path,include
from lost import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('',views.kunallist,name='list'),
     path('create/',views.kunalcreate,name='kunalcreate'),
     path('<int:tweet_id>/edit/',views.edit,name='edit'),
     path('<int:tweet_id>/delete/',views.delete,name='delete'),
     path('register/',views.register,name='register'),
     path('logout/',views.logout,name='logout1'),
     path('login/',views.loginuser,name='login'),
     path('about/',views.about,name='about'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



