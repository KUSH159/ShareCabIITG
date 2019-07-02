from django.urls import path
from . import views

urlpatterns = [
            path('signup/', views.SignUp.as_view(), name='signup'),
            path('<str:username>', views.UserInfo, name = 'user_info'),
            path('<str:username>/update', views.UpdateProfile, name='update_profile'),
        ]
