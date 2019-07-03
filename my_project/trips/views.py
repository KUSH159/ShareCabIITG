from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from accounts.models import UserTrips
from django.utils.timezone import timedelta
# Create your views here.

def MyTrips(request, username):
    user = User.objects.get(username = username)
    trips = user.usertrips_set.all()
    return render(request, 'trips/trips.html', context = {'trips': trips,'user': user,})

def AddTrip(request, username):
    user = User.objects.get(username = username)
    if request.method=="POST":
        trip_datetime = request.POST['datetime']
        if request.POST['choice']=="Camp2Air":
           source = "Campus"
           destination = "Airport"
        elif request.POST['choice']=="Air2Camp":
            source = "Airport"
            destination = "Campus"
        elif request.POST['choice']=="Camp2Rail":
            source = "Campus"
            destination = "Railway Station"
        elif request.POST['choice']=="Rail2Camp":
            source = "Railway Station"
            destination = "Campus"
        trip = user.usertrips_set.create(source=source, destination=destination,trip_datetime=trip_datetime)
        trip.save()
        request.method = "GET"
        return HttpResponseRedirect(reverse('trips:mytrips', args=(username,))) 
    else:
        user = User.objects.get(username = username)
        return render(request, 'trips/addtrip.html', {'user': user,})

def ViewTrip(request,username,trip_id):
    user = User.objects.get(username = username)
    mytrip = UserTrips.objects.get(pk=trip_id)
    src = mytrip.source
    dest = mytrip.destination
    date = mytrip.trip_datetime
    #time = mytrip.trip_datetime.time()
    td = timedelta(hours = 1)
    matched = UserTrips.objects.filter(source = src).filter(destination = dest).exclude(customuser=user)
    matched = matched.filter(trip_datetime__lte=(date+td)).filter(trip_datetime__gte=(date-td))
    return render(request, 'trips/viewtrip.html', {'matched' : matched, 'username' : username, 'trip_id': trip_id,})

def ViewProfile(request,username):
    user = User.objects.get(username = username)
    return render(request, 'profile.html', {'user':user,})
