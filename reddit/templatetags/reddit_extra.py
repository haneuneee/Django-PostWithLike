from datetime import timedelta, timezone
from django import template
from django.utils import timezone
from tzlocal import get_localzone

register = template.Library()


def get_time_difference(value):
    value = value.astimezone(get_localzone())
    now = timezone.now().astimezone(get_localzone())
    try:
        return now - value
    except:
        return value


@register.filter
def check_new(value):
    difference = get_time_difference(value)
    if difference <= timedelta(days=1):
        return True
    else:
        return False

@register.filter
def check_hot(value):
    if value > 0:
        return True
    else:
        return False
@register.filter
def custom_time(value):
    time_str_format = '%Y년 %m월 %d일 %H시 %M분'
    difference = get_time_difference(value)

    if difference <= timedelta(minutes=1):
        # return value.strftime(time_str_format)
        return '방금전'
    elif difference <= timedelta(hours=1):
        # return value.strftime(time_str_format)
        return '%(min)s분전' % {"min": (difference.seconds % 3600) // 60}
    elif difference <= timedelta(days=1):
        # return value.strftime(time_str_format)
        return '%(hour)s시간전' % {'hour': difference.seconds // 3600}
    else:
        return value.strftime(time_str_format)


@register.filter
def up_voted_by(obj, user):
    return obj.up_voted_by(user)


@register.filter
def down_voted_by(obj, user):
    return obj.down_voted_by(user)
