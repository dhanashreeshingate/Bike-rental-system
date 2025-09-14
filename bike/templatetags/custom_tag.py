from django import template
from bike.models import *
register = template.Library()

@register.filter(name = 'notification')
def notification(obj):
    booking = Booking.objects.filter(Status=None)
    return booking

@register.simple_tag()
def notificationcount(*args, **kwargs):
    bookingcount  = Booking.objects.filter(Status=None).count()
    return bookingcount