from django.db import models

# Create your models here.
class Location(models.Model):
    dojo_name = models.CharField(max_length=250, default="Iowa Martial Arts Des Moines")
    address = models.CharField(max_length=250)
    picture_url = models.TextField(default="https://www.google.com/search?hl=en&sxsrf=ALeKk03td3PWu0TAdzw7a2W5BfkIkUmsMw%3A1586357941737&source=hp&ei=teaNXqHHKsaztAaT5qMo&q=3800+Merle+Hay+Rd%2C+Des+Moines%2C+IA+50310&oq=3800+Merle+Hay+Rd%2C+Des+Moines%2C+IA+50310&gs_lcp=CgZwc3ktYWIQAzICCCYyBggAEBYQHjICCCYyBQgAEM0CMgUIABDNAkoJCBcSBTEyLTc0SggIGBIEMTItMVC2FFi2FGDkHGgBcAB4AIABRIgBRJIBATGYAQCgAQKgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwjh9efsi9noAhXGGc0KHRPzCAUQ4dUDCAk&uact=5#")
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