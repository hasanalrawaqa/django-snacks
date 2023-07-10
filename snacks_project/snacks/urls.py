from django.urls import path
from .views import home ,about

urlpatterns = [
    path('', home.as_view(),name='home'),
    path('about', about.as_view(),name='about')
]