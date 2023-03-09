from Register.models import Profession
from django import template
from django.db.models import Count
register = template.Library()


@register.simple_tag(name='get_list_proffesion')
def get_proffesion():
    return Profession.objects.all()


