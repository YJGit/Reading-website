from django import template
from books.models import UserProfile

register = template.Library()

@register.inclusion_tag('user_address.html')

def get_user_address(user=None):
    return {'user_profile': UserProfile.objects.get(user=user)}