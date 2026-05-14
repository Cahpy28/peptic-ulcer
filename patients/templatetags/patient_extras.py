from django import template


register = template.Library()


@register.filter
def badge_class(value):
    return str(value or "low").lower()
