from django.urls import path
from . import views
urlpatterns=[
    # path('home/',views.home,name='home')
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('course_new/',views.course_new,name='course_new'),
    path('dashboard/',views.dashboard,name='dashboard')
]