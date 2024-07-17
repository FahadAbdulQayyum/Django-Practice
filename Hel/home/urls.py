from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Fahad Custom Shop"
admin.site.site_title = "Fahad Custom Shop"
admin.site.index_title = "Welcome to FHD Custom Shop Portal"

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("services", views.services, name="services"),
]
