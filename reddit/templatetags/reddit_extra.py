from datetime import timedelta, timezone
from django import template
from django.utils import timezone
from tzlocal import get_localzone

register = template.Library()


@register.filter
def custom_time(value):
    time_str_format = '%Y년 %m월 %d일 %H시 %M분'
    value = value.astimezone(get_localzone())
    now = timezone.now().astimezone(get_localzone())
    try:
        difference = now - value
    except:
        return value

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
