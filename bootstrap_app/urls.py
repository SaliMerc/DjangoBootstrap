from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='my_index'),
    path('about/',views.about,name='my_about'),
    path('contact/',views.contact,name='my_contact'),
    path('booking/', views.booking, name='my_booking'),
    path('menu/',views.menu,name='my_menu'),
    path('service/',views.service,name='my_service'),
    path('team/',views.team,name='my_team'),
    path('testimonial/',views.testimonial,name='my_testimonial'),


]