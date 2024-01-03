from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Concert(models.Model):
    artist = models.CharField(max_length=30)


class Venue(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=25)


class Performance(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateField('date performed')


class Ticket(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
