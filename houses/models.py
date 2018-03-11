from django.db import models
from django.contrib.auth.models import User

  

class Myhouses(models.Model):
    Available = 'A'
    Not_Available = 'NA'
    Availability = (
        (Available, 'Available'),
        (Not_Available, 'Not_Available'),
    )
    name_of_accomodation = models.CharField(max_length=200)
    type_of_room = models.CharField(max_length=200)
    house_rent = models.IntegerField()
    availability = models.CharField(max_length=2, choices=Availability, default=Available,)
    location = models.CharField(max_length=200)
    nearest_institution = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_image')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='author')

    def __str__(self):
        return self.name_of_accomodation

