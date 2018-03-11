from django.db import models
from django.conf import settings

class Profile(models.Model):    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)    
    date_of_birth = models.DateField(blank=True, null=True)
    nickname = models.CharField(max_length=200, default='gabby')
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):        
        return 'Profile for user {}'.format(self.user.username)

class Houses(models.Model):
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

    def __str__(self):
        return self.name_of_accomodation


class trial(models.Model):
    name = models.TextField()
    likes = models.TextField()

    def __str__(self):
        return self.name
