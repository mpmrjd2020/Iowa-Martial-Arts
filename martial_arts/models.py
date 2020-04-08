from django.db import models

# Create your models here.
class Location(models.Model):
    dojo_name = models.CharField(max_length=250, default="Iowa Martial Arts Des Moines")
    address = models.CharField(max_length=250)
    picture_url = models.TextField(default="https://www.google.com/maps/vt/data=q2HB5TlSWTUrQ4rqKFu-yy5cEqZplqRNBC9Vlu4HOnj15T4-pK8zFMMrAWVuNsxiF7U-Kp26lKHJ93qC_tNlNfJIXe_2HTXxi-sdrD3tnbBt3jzGXPzvVBh1KR-ludu5O0PZ74dzbrNtieq0v4VNmgrp3gJ4zubECA")
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.dojo_name

class Class_Schedule(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Class_Schedules')
    style = models.CharField(max_length=250)
    instructor = models.CharField(max_length=250)
    schedule = models.TextField()

    def __str__(self):
        return self.style