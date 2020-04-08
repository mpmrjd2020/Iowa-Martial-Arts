from django.shortcuts import render
from .models import Location, Class_Schedule

# Create your views here.
def location_list(request):
    locations = Location.objects.all()
    return render(request, 'martial_arts/location_list.html', {'locations': locations})

def class_schedule_list(request):
    class_schedules = Class_Schedule.objects.all()
    return render(request, 'martial_arts/class_schedule_list.html', {'class_schedules': class_schedules})

def location_detail(request, pk):
    location = Location.objects.get(id=pk)
    return render(request, 'martial_arts/location_detail.html', {'location': location})

def class_schedule_detail(request, pk):
    class_schedule = Class_Schedule.objects.get(id=pk)
    return render(request, 'martial_arts/class_schedule_detail.html', {'class_schedule': class_schedule})

