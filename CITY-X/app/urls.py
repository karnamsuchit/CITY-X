
from django.urls import path
from .views import *
urlpatterns = [
    path('home', home, name = 'home'),
    path("booking", booking, name='booking'),
    path('guide_register', guide_register, name='guide_register'),
    path('bengaluru', bengaluru, name='bengaluru'),
    path('mysuru', mysuru, name='mysuru'),
    path('', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('<int:id>', guide_details, name='guide_details'),
]
