from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    attendees_limit = models.IntegerField()
    status = models.BooleanField()
    address = models.CharField(max_length=200)
    start_time = models.DateTimeField('events time')
    create_time = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

    objects = models.Manager() # fix the issue of CustomModel(models.Model) has no attribute 'objects'

    class Meta:
        unique_together = ("event", "phone")

    def __str__(self):
        return self.realname
