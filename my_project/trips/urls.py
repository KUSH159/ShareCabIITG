from django.urls import path
from . import views

app_name = 'trips'
urlpatterns = [
            path('<str:username>', views.MyTrips, name = 'mytrips'),
            path('<str:username>/addtrip', views.AddTrip, name = 'addtrip'),
            path('profile/<str:username>', views.ViewProfile, name = 'viewprofile'),
            path('<str:username>/<str:trip_id>', views.ViewTrip, name = 'viewtrip'), 
        ]
