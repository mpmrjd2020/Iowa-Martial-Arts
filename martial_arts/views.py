from django.shortcuts import render, redirect
from .models import Location, Class_Schedule
from .forms import LocationForm, ClassForm
from django.contrib.auth.decorators import login_required

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

@login_required
def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            location = form.save()
            return redirect('location_detail', pk=location.pk)
    else:
        form = LocationForm()
    return render(request, 'martial_arts/location_form.html', {'form': form})

@login_required
def class_schedule_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            class_schedule = form.save()
            return redirect('class_schedule_detail', pk=class_schedule.pk)
    else:
        form = ClassForm()
    return render(request, 'martial_arts/class_schedule_form.html', {'form': form})

@login_required
def location_edit(request, pk):
    location = Location.objects.get(pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, request.FILES, instance=location, )
        if form.is_valid():
            location = form.save()
            return redirect('location_detail', pk=location.pk)
    else:
        form = LocationForm(instance=location)
    return render(request, 'martial_arts/location_form.html', {'form': form})

@login_required
def class_schedule_edit(request, pk):
    class_schedule = Class_Schedule.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClassForm(request.POST,instance=class_schedule)
        if form.is_valid():
            class_schedule = form.save()
            return redirect('class_schedule_detail', pk=class_schedule.pk)
    else:
        form = ClassForm(instance=class_schedule)
    return render(request, 'martial_arts/class_schedule_form.html', {'form': form})

@login_required
def location_delete(request, pk):
    Location.objects.get(id=pk).delete()
    return redirect('location_list')

@login_required
def class_schedule_delete(request, pk):
    Class_Schedule.objects.get(id=pk).delete()
    return redirect('class_schedule_list')

