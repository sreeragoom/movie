from django.urls import path, include

from . import views
app_name='user_app'

urlpatterns = [

    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('message/',views.message,name='message'),

]