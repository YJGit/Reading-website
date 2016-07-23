from django import template
from books.models import UserProfile

register = template.Library()

@register.inclusion_tag('user_img.html')

def get_user_img(user=None):
    return {'user_profile': UserProfile.objects.get(user=user)}