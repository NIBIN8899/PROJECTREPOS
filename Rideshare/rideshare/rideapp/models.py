from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class CustomUser(User):
    user_ptr = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
        default=1  #
)

class Meta:

 User=get_user_model()

class Ride(models.Model):
    rider = models.CharField(max_length=190)
    driver = models.CharField(max_length=190)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    STATUS_CHOICES = (
        ('REQUESTED', 'Requested'),
        ('ACCEPTED', 'Accepted'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='REQUESTED')
    current_location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_status_display(self):
        return dict(Ride.STATUS_CHOICES)[self.status]