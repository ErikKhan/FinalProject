from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    # fields for the car table
    name = models.CharField(max_length=300)
    model = models.IntegerField()
    horsepower = models.IntegerField()
    description = models.TextField(max_length=5000)
    price = models.IntegerField(default=0)
    
    averageRating = models.FloatField(default=0)
    image = models.URLField(default=None, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Rating(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=5000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
