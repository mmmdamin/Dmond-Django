from django import template

register = template.Library()


@register.simple_tag
def user_has_perm(user, perm_code):
    return user.has_perm(perm_code)
