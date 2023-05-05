from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registration_view, name='registration'),
    path('login/', views.login_user_view, name='login'),

]
