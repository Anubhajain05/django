from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('tinymce/', include('tinymce.urls')),
    path("register/", views.register, name="register"),
    path("<single_slug>", views.single_slug, name="single_slug"),

]