from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='calregister-home'),
    path('about/', views.about, name='calregister-about'),
    path('bookAppointment/', views.bookAppointment, name='calregister-bookAppointment')
]